# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

n = int(input())
sum_nums = 0
list_nums = []

for i in range(1, n + 1):
    result = round((1 + 1 / i) ** i)
    list_nums.append(result)
    sum_nums += result

print(list_nums)
print(sum_nums)
