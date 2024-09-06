import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    prime_count = 0
    num_length = len(num)

    for digit_pos in range(num_length):
        digit = num[num_length - 1 - digit_pos]
        if digit in hex_digits:
            digit_value = hex_digits.index(digit)
        elif digit in primes:
            digit_value = primes.index(digit)
        else:
            continue

        prime_count += (num_length - digit_pos) * 2 ** digit_value

    return prime_count