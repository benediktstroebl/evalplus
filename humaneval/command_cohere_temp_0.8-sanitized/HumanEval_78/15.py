import math
def is_prime(n):
    """Check if a number is a prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # convert hex string to int to simplify computation
    num = int(num, 16)
    count = 0
    for digit in str(num):
        if digit in '2 3 5 7 B D':
            continue
        # convert digit to decimal, check if it is a prime
        if is_prime(int(digit)):
            count += 1
    return count