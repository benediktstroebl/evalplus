import unittest
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    """
    if n < 1:
        raise ValueError("n must be positive")
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    count = 0

    while count < n:
        # Check if the next Fibonacci number is prime
        if is_prime(a):
            return a
        
        # Calculate the next Fibonacci number
        b = a + b
        a = b
        count += 1
    
    # If we reach this line, it means the requested number n is out of range
    return -1