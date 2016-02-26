import usb.core
import usb.util
import time
from pykeyboard import PyKeyboard

# The number of times a number should be outputted by the scale
# before being output to the user.  This is to allow the scale
# to balance before output
BALANCE_TRESHOLD = 100

# These IDs can be found by using `lsusb`
VENDOR_ID = 0x0b67
PRODUCT_ID = 0x555e
device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

k = PyKeyboard()

for cfg in device:
    for intf in cfg:
        if device.is_kernel_driver_active(intf.bInterfaceNumber):
            try:
                device.detach_kernel_driver(intf.bInterfaceNumber)
            except usb.core.USBError as e:
                sys.exit("Could not detatch kernel driver from interface({0}): {1}".format(intf.bInterfaceNumber, str(e)))

endpoint = device[0][(0,0)][0]

data = None

# Thresholds - these are wiped each time the scale is back to ZERO
# Archives each output, to not repeat itself indefinitely
previous = [0]
# Used as threshold to wait for scale to balance before outputting to the user (100 executions by default)
counts = {};

while True:
    try:
        data = device.read(endpoint.bEndpointAddress, endpoint.wMaxPacketSize)
        weight = float(data[4])/100
        weightStr = str(weight)

        if (weight == 0.0):
            previous = []
            counts = {} 
            continue

        if (weightStr not in counts):
            counts[weightStr] = 0;
        else:
            counts[weightStr] = counts[weightStr] + 1;

        if (counts[weightStr] > BALANCE_THRESHOLD and weight not in previous):
            k.type_string(weightStr)
            previous.append(weight)

    except usb.core.USBError as e:
        data = None
        if e.args == ('Operation timed out',):
            continue
