# 1719pankaj
## _Wireless ADB Script



[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Wireless script lets you connect to an adb device over wifi without hassles and the need to write down the same 
commands everytime.


## Features
- Fast AF
- Verbose 
- Powered by Python

## Installation

Wireless Script requires
| Dependency | Download Link |
| ------ | ------ |
| Pyhton 3.6+ | https://www.python.org/downloads/ |
| ADB | https://forum.xda-developers.com/t/official-tool-windows-adb-fastboot-and-drivers-15-seconds-adb-installer-v1-4-3.2588979/ |
| USB Debugging Enabled | https://www.youtube.com/watch?v=Ucs34BkfPB0 |
| AutoHotkey (Optional) | https://www.autohotkey.com/ |


Step 1:

```sh
copy Run.bat and wireless_script.py to a folder
```

Step 2:

```sh
Create a shortcut for Run.bat
```

Step 3:

```sh
now se this shortcut to use Script
```

Step 4 (optional):

```sh
paste AutoHotkeyScript.ahk in startup folder
And follow the instructions inside
Use "Alt+W" shortcut to use Script.
```

## Usage Instructions

- Run Shortcut (or Alt+W)
![alt text](https://github.com/1719pankaj/Utilities/blob/main/enter.png)

- Connect your phone to pc over USB and make sure USB debugging is enabled and connected  (required for the first time)

- Enter the last digit of your android device's local IP address
![alt text](https://github.com/1719pankaj/Utilities/blob/main/andy.jpeg.jpg)

- Hit Enter and your device should be connected
![alt text](https://github.com/1719pankaj/Utilities/blob/main/connected.png)

- Now disconnect the cable and roll
## Development

Want to contribute? Great!

Read CONTRIBUTING.md

## Idiosyncrasies

ADB over wifi is quite a stable connection but the initial connection process is bit finicky (to put it lightly)

- It won't connect unless and untill you have USB debugging setup and connected (for the first time)
- Depending on your device, OEM and mood of ADB gods you'll never need to connect USB debugging ever or maybe connect it for the first 2-3 times or maybe
- Let's say you managed to make it recognise and connects all wireless well Congratulations. but be prepared just in case the lizard overlords decide to throw "device actively refused to connect" error. In that case you go hunt for the cable again.
- Imma put this on record, this behaviour has nothing to do with my tool, its the nature of ADB over wifi and anything based on it will inherit all its flaws and shortcommings.
- Ok all things aside 98% of the time it works flawlessly and you won't have many problems but its my job to let you know.
- Enjoy :)
