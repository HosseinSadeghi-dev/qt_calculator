import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from PySide6.QtUiTools import QUiLoader


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        loader = QUiLoader()
        self.ui = loader.load("form.ui")
        self.ui.show()

        self.number_1 = ''
        self.number_2 = ''
        self.operator = ''
        self.decimal = False
        self.answer = False

        self.ui.clear.clicked.connect(self.clear)
        self.ui.negative.clicked.connect(self.neg)
        self.ui.decimal.clicked.connect(self.dec)
        self.ui.back.clicked.connect(self.back)
        self.ui.percent.clicked.connect(self.percent)

        self.ui.num_0.clicked.connect(self.num0)
        self.ui.num_1.clicked.connect(self.num1)
        self.ui.num_2.clicked.connect(self.num2)
        self.ui.num_3.clicked.connect(self.num3)
        self.ui.num_4.clicked.connect(self.num4)
        self.ui.num_5.clicked.connect(self.num5)
        self.ui.num_6.clicked.connect(self.num6)
        self.ui.num_7.clicked.connect(self.num7)
        self.ui.num_8.clicked.connect(self.num8)
        self.ui.num_9.clicked.connect(self.num9)

        self.ui.add.clicked.connect(self.add)
        self.ui.sub.clicked.connect(self.sub)
        self.ui.divide.clicked.connect(self.div)
        self.ui.mul.clicked.connect(self.mul)

        self.ui.equal.clicked.connect(self.equal)

    # numbers
    def num0(self):
        number = self.ui.display.toPlainText()
        if self.answer:
            number = '0'
            self.answer = False
        if number != '0':
            number += '0'
        self.ui.display.setText(number)

    def num1(self):
        number = self.ui.display.toPlainText()
        if number == '0' or number == '' or self.answer:
            number = '1'
            self.answer = False
        else:
            number += '1'
        self.ui.display.setText(number)

    def num2(self):
        number = self.ui.display.toPlainText()
        if number == '0' or number == '' or self.answer:
            number = '2'
            self.answer = False
        else:
            number += '2'
        self.ui.display.setText(number)

    def num3(self):
        number = self.ui.display.toPlainText()
        if number == '0' or number == '' or self.answer:
            number = '3'
            self.answer = False
        else:
            number += '3'
        self.ui.display.setText(number)

    def num4(self):
        number = self.ui.display.toPlainText()
        if number == '0' or number == '' or self.answer:
            number = '4'
            self.answer = False
        else:
            number += '4'
        self.ui.display.setText(number)

    def num5(self):
        number = self.ui.display.toPlainText()
        if number == '0' or number == '' or self.answer:
            number = '5'
            self.answer = False
        else:
            number += '5'
        self.ui.display.setText(number)

    def num6(self):
        number = self.ui.display.toPlainText()
        if number == '0' or number == '' or self.answer:
            number = '6'
            self.answer = False
        else:
            number += '6'
        self.ui.display.setText(number)

    def num7(self):
        number = self.ui.display.toPlainText()
        if number == '0' or number == '' or self.answer:
            number = '7'
            self.answer = False
        else:
            number += '7'
        self.ui.display.setText(number)

    def num8(self):
        number = self.ui.display.toPlainText()
        if number == '0' or number == '' or self.answer:
            number = '8'
            self.answer = False
        else:
            number += '8'
        self.ui.display.setText(number)

    def num9(self):
        number = self.ui.display.toPlainText()
        if number == '0' or number == '' or self.answer:
            number = '9'
            self.answer = False
        else:
            number += '9'
        self.ui.display.setText(number)

    # Operators
    def add(self):
        self.operator = '+'
        number = self.ui.display.toPlainText()
        if self.number_1:
            self.equal()
        if self.decimal:
            self.number_1 = float(number)
        else:
            self.number_1 = int(number)
        self.answer = True

    def sub(self):
        self.operator = '-'
        number = self.ui.display.toPlainText()
        if self.decimal:
            self.number_1 = float(number)
        else:
            self.number_1 = int(number)
        self.answer = True

    def mul(self):
        self.operator = '*'
        number = self.ui.display.toPlainText()
        if self.decimal:
            self.number_1 = float(number)
        else:
            self.number_1 = int(number)
        self.answer = True

    def div(self):
        self.operator = '/'
        number = self.ui.display.toPlainText()
        if self.decimal:
            self.number_1 = float(number)
        else:
            self.number_1 = int(number)
        self.answer = True

    # Additional Buttons
    def neg(self):
        number = self.ui.display.toPlainText()
        if number[0] == '-':
            number = number.replace("-", "")
        else:
            number = '-' + number
        self.ui.display.setText(number)

    def clear(self):
        self.number_1 = ''
        self.number_2 = ''
        self.decimal = False
        self.answer = False
        self.ui.display.setText('')

    def dec(self):
        number = self.ui.display.toPlainText()
        if number.find('.') == -1:
            number += '.'
            self.decimal = True
        self.ui.display.setText(number)

    def back(self):
        number = self.ui.display.toPlainText()
        if number != '':
            if number[-1] == '.':
                self.decimal = False
            number = number[:-1]
        self.ui.display.setText(number)

    def percent(self):
        number = int(self.ui.display.toPlainText())
        self.ui.display.setText(str(number / 100))
        self.answer = True

    # submit
    def equal(self):
        number = self.ui.display.toPlainText()
        if self.decimal:
            self.number_2 = float(number)
        else:
            self.number_2 = int(number)

        if self.operator == '+':
            self.answer = True
            number = str(self.number_1 + self.number_2)
        elif self.operator == '-':
            self.answer = True
            number = str(self.number_1 - self.number_2)
        elif self.operator == '/':
            self.answer = True
            if self.number_2 == 0:
                number = "Can't divide By zero"
            else:
                number = str(self.number_1 / self.number_2)
        elif self.operator == '*':
            self.answer = True
            number = str(self.number_1 * self.number_2)

        if isinstance(number, int):
            self.number_1 = int(number)
        elif isinstance(number, float):
            self.number_1 = float(number)
        self.ui.display.setText(number)


if __name__ == "__main__":
    app = QApplication([])
    window = Main()
    sys.exit(app.exec())
