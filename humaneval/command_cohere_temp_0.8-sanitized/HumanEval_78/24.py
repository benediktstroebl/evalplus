import math
def is_prime(n):
    """Check is n is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # your code here
    digit = '0123456789ABCDEF'
    count = 0
    for c in num:
        if c.isupper():
            digit = 'ABCDEF'
        elif c.islower():
            digit = '123456789'
        else:
            continue
        count += digit.index(c) if is_prime(int(digit[digit.index(c)])) else 0
    return count