import math
def hex_key(num):
    """
    Determine the number of hexadecimal digits that are primes.
    """
    # translate hex digits to decimal values
    TRANSLATE = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
    }
    # translate input string to decimal values
    num = [TRANSLATE[c.upper()] for c in num if c in TRANSLATE]
    
    # filter for prime numbers
    PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    
    return sum(1 for n in num if n in PRIMES or n == math.floor(math.sqrt(n)) and all(n%i for i in range(3, int(math.sqrt(n)) + 1, 2)) )