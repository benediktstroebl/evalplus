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
    # Convert hexadecimal string to decimal numbers
    num = int(num, 16)
    digits = []
    while num > 0:
        digits.append(num % 16)
        num //= 16
    # Remove non-hexadecimal digits
    digits = [int(d) for d in digits if d in range(10) or d in [11, 13]]
    # Count prime digits
    return sum(1 for d in digits if is_prime(d))