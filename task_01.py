# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется
# разделитель пробел.
# in
# Number of words: 10
#
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба
#
# in
# Number of words: 6
#
# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва
#
# in
# Number of words: -1
#
# out
# The data is incorrect

# from random import choice
#
#
# def new_list():
#     str = ['а', 'б', 'в']
#     my_list = []
#     num = int(input('Количество элементов:'))
#     for j in range(num):
#         s = ''
#         for i in range(3):
#             s = s + choice(str)
#         my_list.append(s)
#     s = (' '.join(my_list))
#     return (s)
#
#
# print(new_list())


from random import sample


def new_list():
    string = 'абв'
    my_list = []
    num = int(input('Количество элементов:'))
    # s = (sample(string, 3) for j in range(num))
    for j in range(num):
        s = sample(string, 3)
        my_list.append(''.join(s))
    print(' '.join(my_list))
    return ' '.join(my_list)

print(new_list().replace('абв ', ''))
