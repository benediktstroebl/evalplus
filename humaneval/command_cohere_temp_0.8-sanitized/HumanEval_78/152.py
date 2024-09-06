import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0

    # remove all non-hexadecimal digits and convert to integer
    num = re.sub('[^A-Fa-f0-9]', '', num)
    num = int(num, 16)

    # check for prime hexadecimal digits in the number
    for digit in hex_digits:
        if digit in primes and (num & pow(int(digit), 2)) == pow(int(digit), 2):
            count += 1

    return count