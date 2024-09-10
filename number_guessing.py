import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import random as rand

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Number Guessing Game")
        self.setLayout(qtw.QVBoxLayout())
        self.show()
        
        # Create a label
        self.label = qtw.QLabel("Guess a number between 1 and 10")
        self.label.setFont(qtg.QFont('Arial', 20))
        self.layout().addWidget(self.label)
        
        # Create a text box
        self.textbox = qtw.QLineEdit()
        self.textbox.setFont(qtg.QFont('Arial', 20))
        self.layout().addWidget(self.textbox)
        
        # Create a button
        self.button = qtw.QPushButton("Guess", clicked = self.clicked)
        self.layout().addWidget(self.button)
        
        # Create a label for the result
        self.result = qtw.QLabel("")
        self.result.setFont(qtg.QFont('Arial', 20))
        self.layout().addWidget(self.result)
        
        
    def clicked(self):
        try:
            user_guess = int(self.textbox.text())
        except ValueError:
            self.result.setText("Please enter an integer between 1 and 10")
            return
        computer_choice = rand.randint(1, 10)
        if user_guess < 1 or user_guess > 10:
            self.result.setText("Please enter a number between 1 and 10")
        elif user_guess == computer_choice:
            self.result.setText(f"You guessed {user_guess} and the computer chose {computer_choice}. You win!")
        else:
            self.result.setText(f"You guessed {user_guess} and the computer chose {computer_choice}. You lose!")
                
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()