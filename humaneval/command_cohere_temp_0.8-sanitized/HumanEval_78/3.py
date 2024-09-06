import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    prime_count = 0

    # check if the number is empty or not a hexadecimal number
    if num == "":
        return 0

    # convert hexadecimal string to an integer to easily manipulate the digits
    num = int(num, 16)

    # count the prime digits by iterating through each digit of the number
    for digit in str(num):
        if digit in hex_digits and int(digit) in primes:
            prime_count += 1

    return prime_count