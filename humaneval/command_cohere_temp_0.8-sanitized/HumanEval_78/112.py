import math
def hex_key(num):
    prime_list = [2, 3, 5, 7, 11, 13, 17]
    count = 0
    for char in num.upper():
        if char in '0123456789ABCDEF':
            digit = int(char)
        else:
            digit = int(char, 16)
        if digit not in prime_list:
            count += 1
    return count