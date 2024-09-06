Here is a self-contained Python script with a function that solves the problem of finding Fibonacci numbers that are prime:
```python
import math
def prime_fib(n):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    >>> returns None if n<0
    """
    if n < 0:
        return None
    if n == 1:
        return 2
    if n == 2:
        return 3
    if n % 2 == 0:
        return None  # Not prime
    # Calculate the sqrt(n(n+1)/2) and make sure it's an integer
    sqrt_n = math.sqrt(n * (n+1)/2)
    if int(sqrt_n) == round(sqrt_n):
        return int(math.fibibonacci(n))
    return None
```

This function calculates the nth Fibonacci number that is prime, and also makes sure the result is an integer. 

It uses the math library for mathematical functions, and the `math.fibibonacci` function to calculate the nth Fibonacci number.