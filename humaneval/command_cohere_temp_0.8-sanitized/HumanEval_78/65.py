import math
def hex_key(num):
    """
    Determine the number of hexadecimal digits that are primes.
    """
    # make sure the input is a string
    num = str(num)
    
    # initialize the counter of interesting digits
    count = 0
    
    # iterate through each digit in the hexadecimal number
    for digit in num:
        # check if the digit is in the correct range and is uppercase
        if digit.isupper() and digit in '0123456789ABCDEF':
            # check if the digit is a prime
            if is_prime(int(digit)):
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