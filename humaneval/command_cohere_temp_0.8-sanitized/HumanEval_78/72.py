import math
def hex_key(num):
    prime_hex = [1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    count = 0
    for char in num.upper():
        if char in '0123456789ABCDEF':
            digit = int(char)
            if digit not in prime_hex:
                count += 1
    return count