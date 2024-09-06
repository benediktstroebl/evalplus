import math
def hex_key(num):
    prime_digits = {'0':0, '1':0, '2':1, '3':1, '4':0, '5':1, '6':0, '7':1, '8':0, '9':0, 'A':1, 'B':1, 'C':1, 'D':1, 'E':0, 'F':0}
    count = 0
    for digit in num.upper():
        count += prime_digits[digit]
    return count