#  Во входной строке записана последовательность чисел через
# пробел. Для каждого числа выведите слово YES
# (в отдельной строке), если это число ранее встречалось
# в последовательности или NO, если не встречалось.

my_list = [1, 2, 3, 2, 3, 4, 2, 6]
meet_before = set()
for i in my_list:
    if i in meet_before:
        print('YES')
    else:
        print('NO')
        meet_before.add(i)