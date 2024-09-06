import math
def hex_key(num):
    prime_list = [2, 3, 5, 7, 11, 13, 17]
    hex_digits = "0123456789ABCDEF"
    count = 0
    for digit in num:
        if digit in hex_digits and int(digit) in prime_list:
            count += 1
    return count