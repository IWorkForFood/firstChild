import sys

from PyQt5.QtWidgets import (
                            QApplication,
                            QLabel,
                            QWidget,
                            QDialog,
                            QFormLayout,
                            QLineEdit,
                            QPushButton,
                            QVBoxLayout
)
from PyQt5.QtCore import QSize, Qt

app = QApplication([])
#передаем sys.argv, чтобы разрешить аргументы командной строки
#для приложения. Но мы не собираемся их использовать
#поэтому передаем пустой список

#создаем виджет Qt
window_object = QWidget()

window_object.setWindowTitle("[Brackets]")

window_object.setFixedSize(QSize(1000, 200))

vertical_layout = QVBoxLayout()

dict_for_arithmetic = {'(':-1,
                       ')':1}

form_layout = QFormLayout()
line_edit = QLineEdit()
form_layout.addRow('Введите строку:', line_edit)
vertical_layout.addLayout(form_layout)
result_text = QLabel('')
vertical_layout.addWidget(result_text)
'''
def get_result():
    entered_text = line_edit.text()
    check_number = is_cbs(entered_text)
    match (check_number):
        case 0:
            vertical_layout.result_text.setText('строка неправильная')
        case 1:
            result_text.setText('необходимо %d изменений'%need_to_move(str))
        case -1:
            result_text.setText('Некорректно введена строка')
'''

button = QPushButton("Проверить строку")

button.clicked.connect(lambda : f())
button.clicked.connect(lambda : is_cbs('()'))

def f():
    entered_text = line_edit.text()

    match (is_cbs(entered_text)):
        case 0:
            result_text.setText('количество необходимых изменений: %d'%need_to_move(entered_text))
        case 1:
            result_text.setText('строка правильная')
        case -1:
            result_text.setText('Некорректно введена строка')


def is_cbs(string) -> bool:

    if string.count('(') + string.count(')') < len(string):
        return -1

    if not string.count('(')//2 == string.count(')')//2:
        return -1

    unclosed_right_brackets = 0
    for current_bracket in string:
        unclosed_right_brackets += dict_for_arithmetic[current_bracket]
        if unclosed_right_brackets > 0:
            return 0
    return 1

def need_to_move(string) -> int:

    if not string.count('(')//2 == string.count(')')//2:
        return -1

    changes_count = 0
    unclosed_right_brackets = 0

    for current_bracket in string:
        new_uncl_count = unclosed_right_brackets + dict_for_arithmetic[current_bracket]
        if (unclosed_right_brackets < new_uncl_count) and (new_uncl_count > 0):
            changes_count += 1
        else:
            unclosed_right_brackets += dict_for_arithmetic[current_bracket]
    return changes_count

vertical_layout.addWidget(button)

window_object.setLayout(vertical_layout)

window_object.show()

#запускаем цикл событий

sys.exit(app.exec_()) #приложение дойдет до сюда только
#тогда, когда мы выйдем из цикла событий





