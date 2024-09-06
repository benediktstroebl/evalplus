import math
def is_prime(n):
    """
    Checks if a number is prime
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
    # convert hex string to int to simplify calculations
    num = int(num, 16)
    count = 0
    for digit in str(num):
        if digit.isupper(): # filter out uppercase A to F
            if is_prime(int(digit)):
                count += 1
    return count