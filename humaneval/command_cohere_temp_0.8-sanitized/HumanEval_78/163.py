def is_prime(num):
    """Check if a number is a prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    count = 0
    for digit in num:
        if digit in '2 3 5 7 B D':  # Corrected to include 'B' and 'D'
            count += is_prime(int(digit))
    return count