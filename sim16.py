#Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
n = int(input())
a = map(int, input().split())
x = int(input())
print(sum(map(lambda z: int(z == x), a)))