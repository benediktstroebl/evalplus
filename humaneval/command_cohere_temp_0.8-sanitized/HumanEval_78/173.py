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
    # convert the string to a list of digits
    digits = list(num)
    count = 0
    for digit in digits:
        if digit.isupper() and is_prime(int(digit)):
            count += 1
    return count