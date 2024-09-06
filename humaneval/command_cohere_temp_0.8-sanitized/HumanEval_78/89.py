import math
def hex_key(num):
    prime_hex = ['2', '3', '5', '7', 'B', 'D']
    count = 0
    for digit in num:
        if digit in prime_hex:
            count += 1
    return count