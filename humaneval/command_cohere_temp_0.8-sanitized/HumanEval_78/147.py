import math
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # Convert hex strings to decimal values
    num = [int(d) for d in num.upper()]
    count = 0
    for n in num:
        # Check if the current digit is a prime
        if is_prime(n):
            # Check if the digit is in the correct range
            if 2 <= n <= F:  # Allow uppercase hex letters
                count += 1
    return count