import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QDialog)


def initUI():
    global window
    window = QWidget()
    window.resize(350, 230)
    window.setWindowTitle('Індекс маси тіла')


    btn = QPushButton('Перейти до введення даних', window)
    btn.resize(btn.sizeHint())  
    btn.move(66, 90)  

    btn.clicked.connect(open_input_window)

    window.show()
    return window

def open_input_window():
    global main_window
    main_window = QDialog()
    main_window.setWindowTitle('Введіть ваші дані')
    layout = QVBoxLayout()

    height_label = QLabel("Введіть ваш ріст (см):")
    layout.addWidget(height_label)
    height_input = QLineEdit()
    layout.addWidget(height_input)

    weight_label = QLabel("Введіть вашу вагу (кг):")
    layout.addWidget(weight_label)
    weight_input = QLineEdit()
    layout.addWidget(weight_input)

    # Кнопка для розрахунку ІМТ
    calc_button = QPushButton('Розрахувати ІМТ')
    layout.addWidget(calc_button)

    main_window.setLayout(layout)

    def calculate_and_show():
        try:
            height = float(height_input.text())
            weight = float(weight_input.text())
            bmi = calculate_bmi(weight, height) 
            main_window.hide() 
            show_result(bmi) 
        except:
            print("Помилка в введених даних" )
    calc_button.clicked.connect(calculate_and_show)

    window.hide()
    main_window.exec_()


def calculate_bmi(weight, height):
    try:
        if height == 0:
            return "Помилка в введених данних"
        height = (height) / 100  
        bmi = (weight) / (height * height)  
        return round(bmi, 2)
    except:
        return "Помилка в введених даних" 


def show_result(bmi):
    result_window = QDialog()
    result_window.resize(500, 300)
    result_window.show()
    result_window.setWindowTitle('Результат ІМТ')
    res_layout = QVBoxLayout()
    result_label = QLabel(f"Ваш ІМТ: {bmi}")
    res_layout.addWidget(result_label)
    if bmi < int(18.5):
        result_clear = QLabel("У вас дефіцит маси тіла.")
    elif bmi < int(25):
        result_clear = QLabel("У вас нормальна маса тіла.")
    elif bmi < int(30):
        result_clear = QLabel("У вас надлишкова маса тіла.")
    elif bmi < int(35):
        result_clear = QLabel("У вас ожиріння 1 ступеню.")
    elif bmi < int(40):
        result_clear = QLabel("У вас ожиріння 2 ступеню.") 
    else:
        result_clear = QLabel("У вас ожиріння 3 ступеню.")
    res_layout.addWidget(result_clear)


    # Кнопка для повернення до введення даних
    btn_return = QPushButton('Спробувати ще раз')
    res_layout.addWidget(btn_return)

    # Кнопка для виходу з програми
    btn_exit = QPushButton('Вихід з програми')
    res_layout.addWidget(btn_exit)

    def retry():
        result_window.hide()  # Ховаємо вікно з результатом
        open_input_window()  # Відкриваємо вікно введення заново

    def exit_program():
        sys.exit()  # Завершуємо програму

    btn_return.clicked.connect(retry)  # Підключення кнопки "Спробувати ще раз"
    btn_exit.clicked.connect(exit_program)  # Підключення кнопки "Вихід з програми"

    result_window.setLayout(res_layout)
    result_window.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = initUI()
    sys.exit(app.exec_())