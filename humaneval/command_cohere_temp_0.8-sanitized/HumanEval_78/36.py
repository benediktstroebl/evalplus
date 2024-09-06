import math
def is_prime(n):
    """Check if a number is a prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # Convert hexadecimal string to decimal numbers
    num = int(num, 16)
    digits = []
    while num > 0:
        digit = num % 16
        digits.append(digit)
        num = num // 16
    # Count non-zero digits that are primes
    count = sum(1 for digit in digits if digit != 0 and is_prime(digit))
    return count