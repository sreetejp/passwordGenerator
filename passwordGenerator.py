import sys
import random
import string
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication)


class PasswordGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Create the UI elements
        length_label = QLabel('Length:')
        self.length_edit = QLineEdit()
        self.password_label = QLabel('Password:')
        self.password_edit = QLineEdit()
        self.password_edit.setReadOnly(True)
        generate_button = QPushButton('Generate')
        generate_button.clicked.connect(self.generate_password)

        # Set up the layout
        length_layout = QHBoxLayout()
        length_layout.addWidget(length_label)
        length_layout.addWidget(self.length_edit)
        password_layout = QHBoxLayout()
        password_layout.addWidget(self.password_label)
        password_layout.addWidget(self.password_edit)
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(generate_button)
        layout = QVBoxLayout()
        layout.addLayout(length_layout)
        layout.addLayout(password_layout)
        layout.addLayout(button_layout)
        self.setLayout(layout)

        # Set the window properties
        self.setWindowTitle('Password Generator')
        self.resize(300, 100)

    def generate_password(self):
        # Get the desired password length
        try:
            length = int(self.length_edit.text())
        except ValueError:
            self.password_edit.setText('Invalid length')
            return

        # Use all printable ASCII characters
        chars = string.printable
        password = ''.join(random.choices(chars, k=length))
        self.password_edit.setText(password)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    generator = PasswordGenerator()
    generator.show()
    sys.exit(app.exec_())
