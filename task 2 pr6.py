n = int(input("На вход программе подаётся одно целое число"))

if n < 0 or n > 36:
    print("Ошибка ввода")
elif n == 0:
    print("Зелёный")
elif(1 <= n <= 10) or (19 <= n <= 28):
    if n % 2 == 0:
        print("Чёрный")
    else:
        print("Красный")
elif(11 <= n <= 18) or (29 <= n <= 36):
    if n % 2 == 0:
        print("Красный")
    else:
        print("Чёрный")