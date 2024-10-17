# Video to Audio Converter

This Python application provides a simple graphical user interface for converting MP4 video files to MP3 audio files.

## Installation Guide

### Windows

1. Install Python:
   - Download Python from [python.org](https://www.python.org/downloads/windows/)
   - Run the installer and make sure to check "Add Python to PATH"

2. Install required libraries:
   - Open Command Prompt
   - Run the following command:
     ```
     pip install moviepy tkinter
     ```

### MacOS

1. Install Python:
   - MacOS comes with Python pre-installed. To ensure you have the latest version:
     - Install Homebrew (if not already installed) by following instructions at [brew.sh](https://brew.sh/)
     - Open Terminal and run:
       ```
       brew install python
       ```

2. Install required libraries:
   - Open Terminal
   - Run the following command:
     ```
     pip3 install moviepy tkinter
     ```

## Pre-requisites (Tech Stack)

- Python 3.x
- moviepy
- tkinter (usually comes pre-installed with Python)

## Usage

1. Run the script:
   - On Windows: Double-click the Python script or run `python video-to-audio-converter.py` in Command Prompt
   - On MacOS: Open Terminal, navigate to the script's directory, and run `python3 video-to-audio-converter.py`

2. Click "Select MP4 File" in the application window
3. Choose an MP4 file from your computer
4. Wait for the conversion to complete
5. The resulting MP3 file will be saved in the same directory as the original MP4 file

## Disclaimer

This software is provided "as is", without warranty of any kind. The authors are not responsible for any data loss or damage that may occur as a result of using this software. Always ensure you have backups of your important files before performing any conversions.
