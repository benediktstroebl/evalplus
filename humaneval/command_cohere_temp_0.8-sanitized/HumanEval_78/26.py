import math
def hex_key(num):
    """
    Determine the number of hexadecimal digits that are primes.
    """
    # adjust the decimal point to the right position
    num = int(num, 16)
    # initialize the counter for prime digits
    count = 0
    # cycle through all digits of the number
    for digit in str(num):
        # adjust the digit to decimal number
        digit = int(digit)
        if is_prime(digit):
            count += 1
    return count
def is_prime(n):
    """
    Check if a number is prime.
    """
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True