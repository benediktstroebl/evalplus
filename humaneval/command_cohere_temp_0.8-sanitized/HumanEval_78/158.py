import re
def hex_key(num):
    """
    Receives a hexadecimal number as a string and counts the number of hexadecimal digits that are primes.
    """
    # convert hexadecimal string to integer
    num = int(num, 16)
    # initialize counter
    count = 0
    # iterate through digits of the number
    for digit in str(num):
        # check if digit is a prime
        if digit in '23579B' or digit in '13': 
            count += 1
    return count