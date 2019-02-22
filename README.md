## USB Scale to Keystrokes Utility
When ran in the background, this utility will read the data transmitted by a USB scale (tested on a Fairbanks Ultegra) into keystrokes.  This was 
built to help automate a weight-based audit system.

Credit
------------
* This useful tutorial by [Steven Snyder] (http://steventsnyder.com/reading-a-dymo-usb-scale-using-python/)

Features
------------
* Instantly outputs (as keystrokes) weight of items from a USB scale
* Currently, only tested on a Fairbanks Ultegra scale.


Requirements
------------
* [PyUSB] (https://sourceforge.net/projects/pyusb/)
* PyKeyboard from [PyUserInput] (https://github.com/SavinaRoja/PyUserInput)

Installation Notes (MacOS)
------------
MacOS (High Sierra) PyUserInput required Quartz

```bash
pip install pyusb
pip install PyUserInput
pip install pyobjc-framework-Quartz
```

Usage
------------

Issue following command in console.  This will run the scale script in the background.

```bash
    # switch to the directory containing the script
    (sudo) python scale.py &
```

Further notes and constants can be found in the the script (scale.py)

Support
-------

[Please open an issue on GitHub](https://github.com/andrewevansmith/usb-scale-to-keystrokes-fairbanks/issues)


License
-------

This software is released under the MIT License. See the bundled
[LICENSE](https://github.com/andrewevansmith/usb-scale-to-keystrokes-fairbanks/blob/master/LICENSE)
file for details.
