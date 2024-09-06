import math
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # convert the string to lowercase to make it case insensitive
    num = num.lower()
    count = 0
    # iterate through each digit in the hex string
    for digit in num:
        # check if the digit is a valid hex digit
        if digit in '0123456789abcdef':
            # if it is, check if the digit is a prime
            if is_prime(int(digit)):
                count += 1
    return count