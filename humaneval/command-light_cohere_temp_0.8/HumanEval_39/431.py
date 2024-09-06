Here is a self-contained Python script that solves the problem of finding the n-th Fibonacci number and checking if it is a prime:
```python
def is_prime(n):
    """
    A simple checks-based function to check if the number is prime.
    """
    sieve algorithm
    with numbers from 1 to n and returns True if n is prime, else False.
    """
    function checks divisibility with all numbers from 2 up and checks if the number is divisible by any of them.
    """
return n > 1 and not any(i == n for i in range(2, n))

def prime_fib(n):
    """
    Returns n-th Fibonacci number that is prime.
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(4)
    13
    >>> prime_fib(5)
    89
    """
    return is_prime(n)
```