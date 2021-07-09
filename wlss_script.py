import os

tcpip = os.popen('adb tcpip 5555')
print(tcpip.read())

devices = os.popen('adb devices')
print(devices.read())

print("Enter # :- ")
num = input()

stream = os.popen('adb connect 192.168.1.'+num+':5555')
output = stream.read()
print(output)

os.popen('pause >nul')
print("Enter to dismiss")
