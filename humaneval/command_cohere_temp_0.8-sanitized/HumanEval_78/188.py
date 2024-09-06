import re
def hex_key(num):
    primes = ['2', '3', '5', '7', '11', '13', '17', '19', '23', '29', '31', '37', '41', '43', '47', '53', '59', '61', '67', '71', '73', '79', '83', '89', '97']
    hex_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    digit_count = 0
    prime_count = 0
    
    if not num:
        return 0
    
    # Separate the hex digits from other characters to count them separately
    digits_only = re.findall(r'[0-9A-F]', num)