# Дан текст: в первой строке записано число строк, далее идут сами строки.
# Определите, сколько различных слов содержится в этом тексте.
# Словом считается последовательность непробельных символов идущих подряд,
# слова разделены одним или большим числом пробелов или символами конца строки.

# Sample Input:

# 4
# She sells sea shells on the sea shore;
# The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore,
# I'm sure that the shells are sea shore shells.

# Sample Output:

# 19

count_str = int(input())
list_words = []

for i in range(count_str):
    for el in input().split():
        list_words.append(el)

print(len(set(list_words)))