import math
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # Convert hex string to decimal numbers
    num = int(num, 16)
    digits = []
    while num > 0:
        digits.append(num % 16)
        num //= 16
    # Count primes among the digits
    count = sum(1 for digit in digits if is_prime(digit))
    return count