#Import required libraries for GUI, timer, font, and system control
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase

#Define a class for the digital clock inheriting from QWidget. Initialize label, timer, and UI
class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self) 
        self.timer = QTimer(self)
        self.initUI()
# Set the window title, geometry, and add the label into a vertical layout    
    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600,400,300,100)
        
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        #Center the text, set font size and color, and change the window background to black
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("font-size:150px;color:hsl(111,100%,50%);")
        self.setStyleSheet("background-color:black;")
        
        #Load a custom font (DS-DIGIT.TTF) and apply it to the clock label
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family,150)
        self.time_label.setFont(my_font)
        #Connect the timer to the update function, run every 1 second and update the time 
        self.timer.timeout.connect(self.Update_time)
        self.timer.start(1000)
        
        self.Update_time()
    #Get the current system time, format it, and display it on the label    
    def Update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
        
#Start the application, create the clock window, and keep it running        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())