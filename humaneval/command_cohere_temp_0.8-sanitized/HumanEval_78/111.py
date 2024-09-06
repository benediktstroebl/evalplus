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
    # convert the string to uppercase
    num = num.upper()
    count = 0
    for digit in num:
        if digit in '2 3 5 7 B D':  # explicit conversion to int
            count += int(digit)
        elif digit in '0 1 2 3 4 5 6 7 8 9 A B C D E F':
            if is_prime(int(digit)):
                count += 1
    return count