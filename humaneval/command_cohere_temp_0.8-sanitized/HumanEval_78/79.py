import math
def hex_key(num):
    """Count the number of hexadecimal digits that are primes."""
    # convert the string to uppercase
    num = num.upper()
    count = 0
    for char in num:
        if char in '2D5773BCDEF':  # hexadecimal digits that are primes
            count += num.count(char)
    return count