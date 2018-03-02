f = open('python.txt')
print(f.read())
f.close()

print("Всем привет!\n")
parol = "123"
login = "Pursik"
a = input("Введите пароль от банка: ")
if a == parol:
        print("Спасибо")
else:
        print("Не врите!")

b = input("Введите логин от банка: ")
if b == login:
        print("Спасибо")
else:
        print("Не врите!")

from mymodule import hi, add, subtraction as sub, divide as div, multiply as mult
hi()
print(add(0, 0))
print(sub(0, 0))
try:
        print(div(0, 0))
except ZeroDivisionError:
        print("Деление на ноль невозможно!")
print(mult(0, 0))       






        




