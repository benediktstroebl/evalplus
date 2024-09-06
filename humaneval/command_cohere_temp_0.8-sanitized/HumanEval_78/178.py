import math
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # convert hex string to int to simplify computation
    num = int(num, 16)
    count = 0
    for c in str(num):
        if c in '0123456789ABCDEF':
            digit = int(c)
            if is_prime(digit):
                count += 1
    return count