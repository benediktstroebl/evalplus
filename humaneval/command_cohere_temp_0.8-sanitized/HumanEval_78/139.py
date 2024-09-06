import math
def hex_key(num):
    prime_hex = [1 for i in range(0, 16) if i not in [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 3, 5, 7]]
    hex_digit = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0
    temp_num = num.upper()
    for i in range(0, len(temp_num)):
        if temp_num[i] in hex_digit:
            count += 1 if prime_hex[int(temp_num[i])] == 1 else 0
    return count