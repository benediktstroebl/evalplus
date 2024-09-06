```python
import math
def prime_fib(n):
    """
    Returns n-th Fibonacci number that is also prime.
    >>> return next((i for i in range(2, n+1) if math.isq(i, i) and i+1 not in math.isPrime))
   
    return 0  # or something non-prime
"""
    return next((i for i in range(2, n+1) if math.isPrime(i) and i+1 not in [2, i]))
``` 
This function uses the `math` module to check if a number is prime and also checks that the next number is not equal to 2, or equal to the input number, to ensure it's a Fibonacci number. The function returns 0 if the `math.isPrime` returns the area that always returns a number greater than 2, so this function will never return 2 or a number less than 3.