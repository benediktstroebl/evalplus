import math
def is_prime(n):
    """Check if a number is a prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # Convert hexadecimal string to decimal numbers
    num = [int(d) for d in num.upper()]
    count = 0
    for n in num:
        # Check if the current digit is not a prime
        if not is_prime(n):
            continue
        # Count digits that are primes, skip duplicates
        for d in range(0, 16):
            if d == n:
                continue
            if is_prime(d):
                count += 1
    return count