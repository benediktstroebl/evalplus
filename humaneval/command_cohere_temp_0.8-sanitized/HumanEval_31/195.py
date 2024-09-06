import unittest
def is_prime(n):
    if n < 2:
        return False
    
    # Check if the number is divisible from 2 to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    return True