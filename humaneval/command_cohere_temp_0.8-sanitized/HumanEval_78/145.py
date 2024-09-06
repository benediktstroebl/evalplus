import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    prime_count = 0

    # Check if the input string is empty
    if num == "":
        return 0

    # Convert hexadecimal string to decimal values
    decimal_num = int(num, 16)

    # Count prime digits and hexadecimal digits
    for d in re.findall(r'[0-9ABCDEF]', num):
        digit_decimal = int(d, 16)
        if digit_decimal in primes:
            prime_count += 1
        elif digit_decimal < 16:
            prime_count += (digit_decimal == decimal_num)

    return prime_count