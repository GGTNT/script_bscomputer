@echo off
cls
if not "%1"=="am_admin" (
    powershell -Command "Start-Process -Verb RunAs -FilePath '%0' -ArgumentList 'am_admin'"
    exit /b
)
.\python310\python.exe main.py
del "C:\Users\Public\Desktop\VLC media player.lnk"
del "C:\Users\Public\Desktop\Acrobat Reader.lnk"
pause