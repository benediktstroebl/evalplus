import math
def is_prime(n):
    """
    Checks if a number is a prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes
    """
    # convert hex string to decimal numbers
    n = int(num, 16)
    # initialize counter
    count = 0
    # loop through each digit in the decimal representation of the hex string
    for digit in str(n):
        # check if the digit is a decimal representation of a hexadecimal digit
        if digit in '0123456789ABCDEF':
            # if the digit is not a prime, continue to the next digit
            if not is_prime(int(digit)):
                continue
        count += 1
    return count