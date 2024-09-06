def is_prime(num):
    """Check if a number is prime."""
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def hex_key(st):
    """Count the number of hexadecimal digits that are primes."""
    digits = "0123456789ABCDEF"
    count = 0
    for digit in st:
        if digit in digits and is_prime(int(digit)):
            count += 1
    return count