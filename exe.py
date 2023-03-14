from distutils.core import setup
import py2exe
import easygui
a=easygui.fileopenbox()
setup(
name = "Meter",
description = "Python-based App",
version = "1.0",
console=[a],
options = {"py2exe": {"bundle_files": 1,"packages":"ctypes","includes": "base64,sys,socket,struct,time,code,platform,getpass,shutil",}},
zipfile = None,
)
