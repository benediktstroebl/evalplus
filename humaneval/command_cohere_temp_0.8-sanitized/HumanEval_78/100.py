import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    prime_hex_digits = [x for x in hex_digits if x in primes]

    return len(list(filter(lambda x: x in prime_hex_digits, re.findall(r'[A-F0-9]', num)) ))