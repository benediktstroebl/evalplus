import re
PRIMES = [2, 3, 5, 7, 11, 13, 17]
def is_prime(n):
    """Checks if a number is prime."""
    if n < 2:
        return False
    for p in PRIMES:
        if n % p == 0:
            return False
    return True
def hex_key(num):
    """Counts the number of hexadecimal digits that are primes."""
    hex_digits = "0123456789ABCDEF"
    count = 0
    for digit in re.findall(r'[A-F][A-F0-9]?' , num):
        if is_prime(int(digit, 16)):
            count += 1
    return count