```python
import math

def prime_fib(n):
    """
    Returns n-th number that is a Fibonacci number and it's also prime.
    >>> print(prime_fib(5))
    """
    if n <= 0:
        return "Invalid input.

    # Initialize thea smallest prime Fibonacci number
    temp = 2
    is_prime = True
    while temp <= n:
        if math.isPrime(temp):
            is_prime = False
        temp += 1

    if is_prime:
        return temp
    else:
        return "No prime Fibonacci number greater than the given input"

# Test the function
print(prime_fib(5))
``` 
This function, `prime_fib`, calculates and returns the n-th Fibonacci number that is prime, where n is a positive integer. It uses ais logic to test if each Fibonacci number is prime, starting from 2 and incrementing by 1 up to the desired result.