# 2. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные
# данные хранятся в отдельных текстовых файлах.
# Алгоритм RLE
#
# in
# Enter the name of the file with the text:
# 'text_words.txt'
# Enter the file name to record:
# 'text_code_words.txt'
# Enter the name of the file to decode:
# 'text_code_words.txt'
#
# out
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vvvvvvvvvvvbbwwPPuuuTTYyWWQQ
#
# out in file
# 'text_words.txt'
# aaaaavvvvvvvvvvvvvvvvvvvvvvvvvvvvvssssDDDdddFFggggOOiiiaa
# vbbwwPPuuuTTYyWWQQ
#
# 'text_code_words.txt'
# 5a29v4s3D3d2F4g2O3i2a1
# 1v2b2w2P3u2T1Y1y2W2Q

from itertools import groupby, starmap
from os import path


def rle_encode(text="text_words.txt", code_text="text_code_words.txt"):
    if path.exists(text) and not path.exists(code_text):
        with open(text) as my_f_1, \
                open(code_text, "a") as my_f_2:
            for i in my_f_1:
                my_f_2.write("".join([f"{len(list(v))}{ch}" for ch, v in groupby(i)]))
    else:
        print("The files do not exist in the system!")
