import math
def is_prime(n):
    """Check is n is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # your code here
    count = 0
    num = str(num)
    # filtering out non-hexadecimal digits and converting to int
    digits = [int(d) for d in num if d in '0123456789ABCDEF']
    for d in digits:
        if is_prime(d):
            count += 1
    return count