import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QFileDialog, QLabel, QVBoxLayout, QTextEdit
from youtube_transcript_api import YouTubeTranscriptApi

## youtube_transcript_api get youtube ID not URl 
## the function is to Split ID from URL 
def get_ytid(url):
    from urllib.parse import urlparse
    url_data = urlparse(url)
    ytid = url_data.query[2:]
    return ytid

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    # gte youtube id 


    def initUI(self):
        self.setGeometry(100, 100, 600, 400)
        self.setWindowTitle('Subtitle Downloader')

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel('Select File or Paste YouTube URL:', self)
        self.layout.addWidget(self.label)

        self.text_input = QLineEdit(self)
        self.layout.addWidget(self.text_input)

        self.select_button = QPushButton('Select File', self)
        self.select_button.clicked.connect(self.selectFile)
        self.layout.addWidget(self.select_button)

        self.subtitle_button = QPushButton('Get Subtitle', self)
        self.subtitle_button.clicked.connect(self.getSubtitle)
        self.layout.addWidget(self.subtitle_button)

        self.label = QLabel('Editing in the text view will be considred :', self)
        self.layout.addWidget(self.label)

        self.label = QLabel('Please edit the text section only only :)', self)
        self.layout.addWidget(self.label)

        self.text_view = QTextEdit(self)
        self.layout.addWidget(self.text_view)

        self.save_button = QPushButton('Save Text', self)
        self.save_button.clicked.connect(self.saveText)
        self.layout.addWidget(self.save_button)

    def selectFile(self):
        file_path, _ = QFileDialog.getOpenFileName(self, 'Select File')
        if file_path:
            self.text_input.setText(file_path)
            self.updateTextView(file_path)

    

    def updateTextView(self, text):
        self.text_view.setText(text)

    def getSubtitle(self):
        input_text = self.text_input.text()
        # If video has a transcript or subtitale available# save in txt file

        ytid = get_ytid(input_text)
        transcript = YouTubeTranscriptApi.get_transcript(ytid)
        text = str(transcript)

        self.updateTextView(text)



    def saveText(self):
        text = self.text_view.toPlainText()
        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Text', '', 'Text Files (*.txt);;SubRip Files (*.srt)')
        if file_path:
            file_ext = file_path.split('.')[-1]
            with open(file_path, 'w') as file:
                if file_ext == 'txt':
                    file.write(text)
                elif file_ext == 'srt':
                    converted_text = self.convertToSrt(text)
                    file.write(converted_text)

    def convertToSrt(self, text):
        subtitles = ''
        counter = 1
        for subtitle in eval(text):
            start_time = self.formatTime(subtitle['start'])
            end_time = self.formatTime(subtitle['start'] + subtitle['duration'])
            subtitles += f"{counter}\n{start_time} --> {end_time}\n{subtitle['text']}\n\n"
            counter += 1
        return subtitles

    def formatTime(self, time):
        hours = int(time // 3600)
        minutes = int((time % 3600) // 60)
        seconds = int(time % 60)
        milliseconds = int((time % 1) * 1000)
        return f"{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}"
    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
