import re
PRIMES = {'2', '3', '5', '7', 'A', 'B', 'D', 'E'}
def hex_key(num):
    return sum(1 for x in re.findall('[A-PF0-9]', num.upper()) if x in PRIMES)