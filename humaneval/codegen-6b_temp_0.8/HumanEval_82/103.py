
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    primes = [2,3,5,7,11,13,17,19]
    n = int(string)
    for i in range(len(primes)):
        if n % primes[i] == 0:
            return False
    return True

import unittest