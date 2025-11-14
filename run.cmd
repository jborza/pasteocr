@echo off
REM Start server batch script (Windows CMD)
SETLOCAL

REM Directory of this script
cd /d "%~dp0"

REM Virtualenv directory name (change if needed)
SET VENV_DIR=.venv

REM If venv doesn't exist, create it and install requirements
IF NOT EXIST "%VENV_DIR%\Scripts\activate.bat" (
  echo Virtual environment not found. Creating %VENV_DIR%...
  python -m venv "%VENV_DIR%"
  call "%VENV_DIR%\Scripts\activate.bat"
  if exist requirements.txt (
    echo Installing Python requirements...
    pip install --upgrade pip
    pip install -r requirements.txt
  ) else (
    echo No requirements.txt found, skipping pip install.
  )
) ELSE (
  REM Activate the existing venv
  call "%VENV_DIR%\Scripts\activate.bat"
)

echo Starting Uvicorn (Ctrl+C to stop)...
REM Use python -m uvicorn to ensure uvicorn runs with the venv interpreter
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000

REM Keep the window open after uvicorn exits (remove if not desired)
pause