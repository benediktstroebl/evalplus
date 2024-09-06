import math
def is_prime(n):
    """Check if a number is a prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    hex_digits = '0123456789ABCDEF'
    count = 0
    for char in num:
        if char.isupper():
            digit = hex_digits.index(char)
        else:
            digit = int(char)
        if is_prime(digit):
            count += 1
    return count