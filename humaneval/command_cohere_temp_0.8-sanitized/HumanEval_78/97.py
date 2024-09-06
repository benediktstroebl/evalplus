import math
def is_prime(n):
    """
    Checks if a number is a prime
    """
    if n < 2:
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
    # assuming the input is always correct or empty string
    # converting to lowercase to make it case insensitive
    num = num.lower()
    for digit in num:
        if digit in '23579bde':
            if is_prime(int(digit)):
                count += 1
    return count