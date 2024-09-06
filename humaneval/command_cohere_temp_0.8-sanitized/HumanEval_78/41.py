import math
def hex_key(num):
    prime_hex = [2, 3, 5, 7, 11, 13, 17]
    hex_digits = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    count = 0
    for digit in hex_digits:
        if digit in prime_hex:
            if num.upper().find(digit) > -1:
                count += 1
    return count