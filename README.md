# PDF to MP3 CLI

This repository contains a Python script for a command-line interface (CLI) application that converts the text content of a PDF file into an MP3 file. It's suitable for users who are comfortable with command-line operations and scripting.

The CLI version is ideal for batch processing and can be easily integrated into other software workflows.

## How it Works

The script uses the `PyPDF2` library to extract text from PDF files and the `pyttsx3` library to convert the extracted text into speech. The speech is then saved as an MP3 file, and a transcript of the text is saved as a `.txt` file.

## Usage

To use the script:

1. Place your PDF files in the `input` directory.
2. Run the `app.py` script from the command line.
3. The script will create a separate folder for each PDF file in the `output` directory, containing both an MP3 file and a transcript.

## Requirements

- Python 3.6 or higher
- PyPDF2
- pyttsx3

Install the necessary libraries with pip:

```bash
pip install PyPDF2 pyttsx3
```

### Windows (Important)

This app uses VLC runtime libraries for audio playback.

Before running `PDF-to-MP3-UI.exe`, make sure:

1. **VLC Media Player is installed**  
   Download from the official site: [https://www.videolan.org/vlc/](https://www.videolan.org/vlc/)
2. **Architecture matches**  
   - 64-bit app ↔ 64-bit VLC  
   - 32-bit app ↔ 32-bit VLC
3. `libvlc.dll` is present in your VLC installation directory (for example):
   - `C:\Program Files\VideoLAN\VLC\libvlc.dll`
   - `C:\Program Files (x86)\VideoLAN\VLC\libvlc.dll`
   If you installed VLC to a custom location, ensure `libvlc.dll` exists in that install directory.

If VLC is not installed or not found, the app may fail to start with a `libvlc.dll` error.

## License

This project is open-source and available under the MIT License.

---

For those preferring a graphical interface, check out the [PDF-to-MP3-UI](https://github.com/IPandral/PDF-to-MP3-UI) repository, which provides a user-friendly interface for converting PDFs to MP3 files.