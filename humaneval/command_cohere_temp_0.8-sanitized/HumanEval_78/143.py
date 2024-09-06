import math
def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # Convert hex strings to decimal numbers
    decimal = {char: int(char, 16) for char in num}
    total = 0
    for digit in decimal.values():
        if is_prime(digit):
            total += 1
    return total