@ECHO OFF
CD packages
python-2.7.3.msi
wxPython2.8-win32-unicode-2.8.12.1-py27.exe
pywin32-218.win32-py2.7.exe
SETX /M PATH="C:\Python27;C:\Python27\Scripts;"
CD xlrd-0.9.2
setup.py install
CD ..\XlsxWriter-master
setup.py install
CD ..