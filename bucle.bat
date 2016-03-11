@echo off
FOR /L %%A IN (1,1,10) DO (
  ECHO %%A
  start bucle.bat
)
pause
