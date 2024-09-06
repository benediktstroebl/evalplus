import math
def is_prime(n):
    """Check if a number is a prime."""
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # Convert hexadecimal string to integer to simplify computations
    num = int(num, 16)
    count = 0
    for digit in str(num):
        if digit in '2 3 5 7 B D':  # Corrected comparison with decimal values
            count += is_prime(int(digit))
    return count