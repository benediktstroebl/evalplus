import re
PRIMES = [2, 3, 5, 7, 11, 13, 17]
def hex_key(num):
    prime_count = 0
    digits = [int(d) for d in re.findall('[0-9ABCDEF]', num)]
    for d in digits:
        if d in PRIMES:
            prime_count += 1
    return prime_count