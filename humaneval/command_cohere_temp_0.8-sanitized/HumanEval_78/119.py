import math
def hex_key(num):
    """
    Determine the number of hexadecimal digits that are primes.
    """
    # make sure the input is a string
    num = str(num)
    
    # initialize the counter of interesting digits
    count = 0
    # iterate through the input string char by char
    for c in num:
        # check if the char is in the range from 'A' to 'F'
        if c in ['A','B','C','D','E','F']:
            # convert the char to its decimal representation
            digit = int(c) - 10
            # check if the decimal representation is a prime
            if is_prime(digit):
                count += 1
        # check if the char is in the range from '0' to '9'
        elif c in ['0','1','2','3','4','5','6','7','8','9']:
            # check if the decimal representation is a prime
            if is_prime(int(c)):
                count += 1
    # return the final count
    return count
def is_prime(n):
    """
    Check if a number is prime.
    """
    # simple cases
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True