# -*- coding:utf-8 -*-
import os
import pythoncom
from win32com.shell import shell    
from win32com.shell import shellcon 
def createShortcutLnk(filename,lnkname):
    cpath = os.getcwdu()
    filename = os.path.join(*[cpath,"src",filename])
    shortcut = pythoncom.CoCreateInstance(    
        shell.CLSID_ShellLink, None,    
        pythoncom.CLSCTX_INPROC_SERVER, shell.IID_IShellLink)    
    shortcut.SetPath(filename)    
    if os.path.splitext(lnkname)[-1] != '.lnk':    
        lnkname += ".lnk"
    # get desktop path
    lnkname = os.path.join(*[cpath,lnkname])
    shortcut.QueryInterface(pythoncom.IID_IPersistFile).Save(lnkname,0)   
if __name__ == '__main__':
    
    createShortcutLnk(u"MasterUI.py",u"词法分析系统")
