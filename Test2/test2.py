# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

n = int(input("Введите число: \n"))
a = 1
for i in range(n):
    a *= i + 1
    print(a, end = ", ")

