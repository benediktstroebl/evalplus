import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0

    # check for incorrect symbols and numbers that are not hexadecimal
    if re.search(r'[^A-Fa-f0-9]', num):
        return "Invalid hexadecimal number"

    for char in num:
        if char in hex_digits:
            digit = hex_digits.index(char)
            if primes[digit]:
                count += 1

    return count