# Subtitle Downloader App Documentation
The Subtitle Downloader app is a Python application built with PyQt5 that allows users to select a file or paste a YouTube URL, extract the subtitle text from the input, and save it in either .txt or .srt format.

![image](https://github.com/MustafaAlahmid/Subtitle_Downloader_App_Documentation/assets/39446930/89b3f5a8-d720-4eb1-a256-449c6204023a)



### Installation

Install following libraries 


> pip install pyqt5
> pip install youtube-transcript-api


### Usage
Run the Application: Open a command prompt or terminal, navigate to the directory where you downloaded the source code, and run the following command:
### Copy code
> python app.py

or 
convert it to .exe using 
install pyinstaller 
> pip install pyinstaller

Convert app to .exe
> pyinstaller --onefile --noconsole app.py


### App Interface: The Subtitle Downloader app window will open, displaying the following components:

"Select File or Paste YouTube URL" label: Indicates the purpose of the text input field.
Text Input Field: Allows you to enter a file path or YouTube URL.
"Select File" Button: Click to open a file selection dialog and choose a file.
"Get Subtitle" Button: Click to extract the subtitle text from the input.
Text View: Displays the extracted subtitle text.
"Save Text" Button: Click to save the subtitle text in the selected format (.txt or .srt).

### Currently not supported 
Select File: To select a file, either click the "Select File" button or manually enter the file path or YouTube URL into the text input field and click the "Get Subtitle" button.

Extract Subtitle: After selecting a file or pasting a YouTube URL, click the "Get Subtitle" button to extract the subtitle text. The extracted text will be displayed in the Text View area.

Save Subtitle: Click the "Save Text" button to save the extracted subtitle text. A file selection dialog will open, allowing you to choose the location and file name for the saved file. You can choose either .txt or .srt format for the saved file using the file extension.


