import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    prime_count = 0
    num_length = 0

    if num:
        num_length = len(num)
        for digit in num:
            if digit in hex_digits:
                digit_as_int = int(digit, 16)
                if digit_as_int in primes:
                    prime_count += 1
    return prime_count / num_length