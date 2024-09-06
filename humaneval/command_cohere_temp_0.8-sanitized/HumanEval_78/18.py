import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0

    # Note: the .upper() below is intentional, to match uppercase symbols
    # A, B, C, D, E, F
    if re.search('^[0-9]+$', num.upper()):
        num = int(num, 16)
        for digit in str(num):
            if digit in hex_digits and int(digit) in primes:
                count += 1
    elif re.search('^[A-F]+$', num.upper()):
        num = int(num, 16)
        for digit in str(num):
            if digit in hex_digits[8:].upper() and int(digit) in primes:
                count += 1
    return count