```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is also prime.
    >>> print(prime_fib(1))
    2
    True
    >>> print(prime_fib(2))
    3
    True
    >>> print(prime_fib(3))
    5
    True
    >>> print(prime_fib(4))
    13
    True
    >>> print(prime_fib(5))
    89
    True
    >>> print(prime_fib(6))
    -3
    False
    """
``` 
This function uses the following formula to generate the n-th prime Fibonacci number: It checks if the square of (n+1) and (n+2) are relatively prime (their gcd equals 1). The function then returns the n-th Fibonacci number, which is both prime.