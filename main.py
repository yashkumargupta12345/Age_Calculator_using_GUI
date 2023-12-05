from PyQt6.QtWidgets import QApplication, QLabel, QWidget,  QGridLayout, \
                            QLineEdit, QPushButton
from datetime import datetime
import sys


class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()
        date_of_birth_label = QLabel("Date of Birth:")
        self.date_birth_line_edit = QLineEdit()

        calculate_button = QPushButton('Calculate age')
        calculate_button.clicked.connect(self.age)
        self.output_label = QLabel('')

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(date_of_birth_label, 1, 0)
        grid.addWidget(self.date_birth_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

    def age(self):
        currentyear = datetime.now().year
        dateofbirth = self.date_birth_line_edit.text()
        yearofbirth = datetime.strptime(dateofbirth, "%m/%d/%Y").date().year
        Age = currentyear - yearofbirth
        self.output_label.setText(f"{self.name_line_edit.text()} is {Age} years old")

app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())

