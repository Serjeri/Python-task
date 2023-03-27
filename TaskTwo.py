""" Задача 2.
Дано целое положительное число "num", представленное в виде строки, и целое
число "k". Вернуть минимальное возможное число, полученное после удаления из
строки k цифр.
Примеры:
Дано: num = "1432219", k = 3
Результат: "1219"
Дано: num = "10200", k = 1
Результат: "200" """

num = "1432219"
k = 3

numbers = len(num)

stack = []
for i in range(numbers):
    if len(stack) == 0:
        stack.append(num[i])
    else:
        if len(stack) > 0 and int(num[i]) < int(stack[-1]) and len(stack) >= i - k + 1:
            stack.pop()
        if len(stack) == 0 or len(stack) < numbers - k:
            stack.append(num[i])
print(str(int("".join(stack))))
