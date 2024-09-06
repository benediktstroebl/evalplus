import pytest
def is_prime(n):
    """
    Checks if a number is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    """
    # Ensure n is positive
    n = abs(n)
    # Initialize variables for the first two Fibonacci numbers
    a, b = 0, 1
    count = 0
    while count < n:
        # Store the current Fibonacci number
        temp = b
        b = a + b
        a = temp
        count += 1
        
        # Check if the current Fibonacci number is prime
        if is_prime(a):
            return a
    
    # If we reach this point, the loop hasn't found a prime Fibonacci number in 'n' iterations.
    # Assuming `n` is large, the next Fibonacci number would be larger than `n`,
    # so it would have been found in the loop above. However, as a failsafe,
    # return the next Fibonacci number after 'n' iterations to avoid an infinite loop.
    return a