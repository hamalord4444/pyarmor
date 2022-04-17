#/usr/bin/python3
#Created By xXx_not_found_xXx
'''
*_> pyarmor encryption for python3
*_> support mobile and pc
*_> after you encrypted your file.py go to location dist folder and take your file.py encrypted and pytransform folder with files in here...
'''

import os
try:
    os.system('pip install python2')
    os.system('pip install python3')
    os.system('pip3 install python2')
    os.system('pip3 install python3')
    os.system('pip2 install pyarmor')
    os.system('pip3 install pyarmor')
except ImportError and ImportWarning:
    os.system('pip install python2')
    os.system('pip install python3')
    os.system('pip3 install python2')
    os.system('pip3 install python3')
    os.system('pip2 install pyarmor')
    os.system('pip3 install pyarmor')

os.system('clear')
File = input('Enter Location Your File > ')
os.system('pyarmor o ' + File)
print('In Mobile File Saved In > /sdcard/dist')
print('In Linux File Saved In > /home/dist')