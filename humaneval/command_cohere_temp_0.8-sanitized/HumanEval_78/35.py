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
    # your code here
    count = 0
    num = str(num)
    # assuming input is always correct or empty string
    # converting to lowercase to make it case insensitive
    num = num.lower()
    for digit in num:
        if digit in '2 3 5 7 b d':
            if is_prime(int(digit)):
                count += 1
    return count