# ==========================================
# Импорт библиотек
# ==========================================
import tkinter as tk
import sqlite3
from tkinter import messagebox

# ==========================================
# Подключение к базе данных
# ==========================================
def connect_db():
    return sqlite3.connect("northwind.db")


# ==========================================
# Выполнение SELECT-запроса
# ==========================================

def run_select(query):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.close()
        return result
    except Exception as e:
        messagebox.showerror("SQL ошибка", str(e))
        return []


def show_result(result):
    output.delete(1.0, tk.END)
    if not result:
        output.insert(tk.END, "Нет данных\n")
    for row in result:
        output.insert(tk.END, str(row) + "\n")


# ==========================================
# Функции для кнопок
# ==========================================

def select_1():
    query = "SELECT CustomerID, CompanyName, Country FROM Customers;"
    show_result(run_select(query))


def select_2():
    query = "SELECT OrderID, OrderDate, ShipCountry FROM Orders LIMIT 20;"
    show_result(run_select(query))


def select_3():
    query = "SELECT ProductName, UnitPrice FROM Products WHERE UnitPrice > 50;"
    show_result(run_select(query))


def select_4():
    query = "SELECT DISTINCT Country FROM Customers;"
    show_result(run_select(query))


def select_5():
    query = "SELECT COUNT(*) FROM Orders;"
    show_result(run_select(query))


# ---------- ОКНО ----------

window = tk.Tk()
window.title("SQL кнопки (Northwind)")
window.geometry("700x450")

tk.Button(window, text="Все клиенты", command=select_1).pack(pady=3)
tk.Button(window, text="Заказы (20)", command=select_2).pack(pady=3)
tk.Button(window, text="Дорогие товары", command=select_3).pack(pady=3)
tk.Button(window, text="Страны клиентов", command=select_4).pack(pady=3)
tk.Button(window, text="Кол-во заказов", command=select_5).pack(pady=3)

output = tk.Text(window, height=15, width=85)
output.pack(pady=10)

window.mainloop()

