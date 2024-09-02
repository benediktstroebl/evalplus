
def prime_length(string):
    """Write a function that takes a string and returns True if the string
    length is a prime number or False otherwise
    Examples
    prime_length('Hello') == True
    prime_length('abcdcba') == True
    prime_length('kittens') == True
    prime_length('orange') == False
    """
    if len(string) < 2:
        return True
    for i in range(2, len(string)):
        if string[0:i] == string[i:2*i]:
            return False
    return True
    
import unittest
