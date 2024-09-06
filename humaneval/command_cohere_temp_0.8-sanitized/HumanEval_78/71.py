import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    count = 0

    # check if input is an empty string or a correct hexadecimal number
    if num in ([]):
        print('0')
        return 0

    # hexadecimal number can contain digits and letters only
    if re.search("[^0-9A-Fa-f]", num):
        print('0')
        return 0

    for char in num:
        if char in hex_digits:
            digit = hex_digits.index(char)
        else:
            digit = primes.index(char)

        # if the digit is a prime, or a hexadecimal digit that corresponds to a prime number, count it
        if digit != -1:
            count += 1

    return count