import math
def hex_key(num):
    prime_hex = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 5, 7, 0, 1, 3, 5, 7]
    count = 0

    for c in num:
        if c.isupper():
            count += prime_hex[int(c)]

    return count