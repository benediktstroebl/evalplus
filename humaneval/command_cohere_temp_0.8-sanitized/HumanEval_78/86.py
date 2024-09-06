import math
def hex_key(num):
    prime_list = [2, 3, 5, 7, 11, 13, 17]
    hex_digit_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0
    for digit in hex_digit_list:
        if digit in prime_list:
            if num.upper().count(digit) > 0:
                count += num.upper().count(digit)
    return count