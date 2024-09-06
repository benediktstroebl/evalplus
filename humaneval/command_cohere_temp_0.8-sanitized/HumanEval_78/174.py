def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # Convert hexadecimal string to integer
    num = int(num, 16)
    # Count digits that are primes
    count = 0
    for c in str(num):
        if c.isupper() and is_prime(int(c, 16)):
            count += 1
    return count