import math
def hex_key(num):
    prime_hex = [1 for i in range(0, 16) if i not in [10, 12, 14, 15]]
    hex_count = 0
    num = str(num)

    for i in range(0, len(num)):
        if num[i] in prime_hex:
            hex_count += 1

    return hex_count