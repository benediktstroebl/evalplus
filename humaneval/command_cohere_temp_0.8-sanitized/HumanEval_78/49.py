import math
def is_prime(n):
    """Check if a number is a prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # Convert hexadecimal string to decimal values
    num = int(num, 16)
    digit_count = 0
    num_str = str(num)
    for digit in num_str:
        if digit.isalpha():
            if is_prime(int(digit, 16)):
                digit_count += 1
    return digit_count