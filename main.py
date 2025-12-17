# ==========================================
# Импорт библиотек
# ==========================================

import tkinter as tk      # библиотека для создания графического интерфейса
import sqlite3            # библиотека для работы с SQLite


# ==========================================
# Подключение к базе данных
# ==========================================

def connect_db():
    """
    Подключаемся к базе данных.
    Файл базы данных должен лежать рядом с этим файлом.
    """
    return sqlite3.connect("database.db")


# ==========================================
# Выполнение SELECT-запроса
# ==========================================

def run_select(query):
    """
    Выполняет SELECT-запрос и возвращает результат
    """
    conn = connect_db()        # подключаемся к БД
    cursor = conn.cursor()     # создаём курсор

    cursor.execute(query)     # выполняем SQL-запрос
    result = cursor.fetchall()# получаем результат

    conn.close()               # закрываем соединение
    return result


# ==========================================
# Функции для кнопок
# ==========================================

def select_1():
    """
    SELECT-запрос №1
    """
    output.delete(1.0, tk.END)  # очищаем поле вывода

    # ❗ СТУДЕНТ ПИШЕТ ЗАПРОС ЗДЕСЬ
    query = "SELECT * FROM students;"

    result = run_select(query)

    for row in result:
        output.insert(tk.END, str(row) + "\n")


def select_2():
    """
    SELECT-запрос №2
    """
    output.delete(1.0, tk.END)

    # ❗ СТУДЕНТ ПИШЕТ ЗАПРОС ЗДЕСЬ
    query = "SELECT name, age FROM students;"

    result = run_select(query)

    for row in result:
        output.insert(tk.END, str(row) + "\n")


def select_3():
    """
    SELECT-запрос №3
    """
    output.delete(1.0, tk.END)

    # ❗ СТУДЕНТ ПИШЕТ ЗАПРОС ЗДЕСЬ
    query = "SELECT * FROM students WHERE age > 18;"

    result = run_select(query)

    for row in result:
        output.insert(tk.END, str(row) + "\n")


def select_4():
    """
    SELECT-запрос №4
    """
    output.delete(1.0, tk.END)

    # ❗ СТУДЕНТ ПИШЕТ ЗАПРОС ЗДЕСЬ
    query = "SELECT DISTINCT group_name FROM students;"

    result = run_select(query)

    for row in result:
        output.insert(tk.END, str(row) + "\n")


def select_5():
    """
    SELECT-запрос №5
    """
    output.delete(1.0, tk.END)

    # ❗ СТУДЕНТ ПИШЕТ ЗАПРОС ЗДЕСЬ
    query = "SELECT COUNT(*) FROM students;"

    result = run_select(query)

    for row in result:
        output.insert(tk.END, str(row) + "\n")


# ==========================================
# Создание окна
# ==========================================

window = tk.Tk()
window.title("SELECT-запросы к базе данных")
window.geometry("600x400")


# ==========================================
# Кнопки
# ==========================================

tk.Button(window, text="SELECT 1", command=select_1).pack(pady=3)
tk.Button(window, text="SELECT 2", command=select_2).pack(pady=3)
tk.Button(window, text="SELECT 3", command=select_3).pack(pady=3)
tk.Button(window, text="SELECT 4", command=select_4).pack(pady=3)
tk.Button(window, text="SELECT 5", command=select_5).pack(pady=3)


# ==========================================
# Поле вывода результата
# ==========================================

output = tk.Text(window, height=12, width=70)
output.pack(pady=10)


# ==========================================
# Запуск программы
# ==========================================

window.mainloop()
