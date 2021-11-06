# 7. Напишите программу на python, которая запрашивает у пользователя 3 целых числа и
# выводит на экран только те числа, которые принадлежат интервалу (10, 20]. Реализовать
# обработку исключений.

try:
    number1 = int(input("Введите первое целое число (10, 20]: "))
    number2 = int(input("Введите второе целое число (10, 20]: "))
    number3 = int(input("Введите третье целое число (10, 20]: "))

    if (number1<10 or number2<10 or number3<10):
        raise Exception("Числа должны быть больше 10")
    if (number1>21 or number2>21 or number3>21):
        raise Exception("Числа должны быть меньше 21")
    print("первое число: ", number1)
    print("второе число: ", number2)
    print("третье число: ", number3)

except ValueError:
    print("Unsupported number format")
except Exception as e:
    print(e.args[0])
