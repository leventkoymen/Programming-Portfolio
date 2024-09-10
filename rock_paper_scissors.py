import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg
import random as rand

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rock Paper Scissors")
        self.setLayout(qtw.QVBoxLayout())
        self.show()
        user_choice = None
        
        # Create a label
        self.label = qtw.QLabel("Make your move")
        self.label.setFont(qtg.QFont('Arial', 20))
        self.layout().addWidget(self.label)
        
        # Create three buttons
        rock_button = qtw.QPushButton("Rock", clicked = lambda: self.clicked("rock"))
        paper_button = qtw.QPushButton("Paper", clicked = lambda: self.clicked("paper"))
        scissors_button = qtw.QPushButton("Scissors", clicked = lambda: self.clicked("scissors"))
        
        # Add buttons to layout
        self.layout().addWidget(rock_button)
        self.layout().addWidget(paper_button)
        self.layout().addWidget(scissors_button)
        
        
    def clicked(self, text):
        computer_choice = rand.choice(["rock", "paper", "scissors"])
        if text == computer_choice:
            self.label.setText(f"You picked {text} and the computer picked {computer_choice}. It's a tie!")
        elif (text == "rock" and computer_choice == "scissors") or (text == "paper" and computer_choice == "rock") or (text == "scissors" and computer_choice == "paper"):
            self.label.setText(f"You picked {text} and the computer picked {computer_choice}. You win!")
        else:
            self.label.setText(f"You picked {text} and the computer picked {computer_choice}. You lose!")


app = qtw.QApplication([])
mw = MainWindow()
app.exec_()

        