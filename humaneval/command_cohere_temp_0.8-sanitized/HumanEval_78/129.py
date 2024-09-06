import re
PRIMES = [2, 3, 5, 7, 11, 13, 17]
def hex_key(num):
    prime_count = sum(x in num for x in PRIMES)
    return len(re.findall("[02357ABCDEF]", num)) - prime_count