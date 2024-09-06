import unittest
def hex_key(num):
    """
    Counts the number of hexadecimal digits that are primes.
    """
    count = 0
    for char in num:
        if char.isupper():
            digit = int(char)
            if is_prime(digit):
                count += 1
    return count