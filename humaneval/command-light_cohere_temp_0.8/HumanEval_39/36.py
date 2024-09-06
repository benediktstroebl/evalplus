```python
def prime_fib(n: int):
    """
    Returns n-th Fibonacci number that is prime.
    >>> prime_fib(1)
    2
    True
    >>> prime_fib(2)
    3
    True
    >>> prime_fib(3)
    5
    True
    >>> prime_fib(5)
    89
    False
    >>> prime_fib(6)
    24
    False
    >>> prime_fib(10)
    248
    True
    >>> prime_fib(100)
    True
    """
    return next((i for i in range(2, n+1) if is_prime(i)))

def is_prime(n: int):
    """
    Check if n is prime
    >>> is_prime(0)
    False
    >>> is_prime(1)
    False
    >>> is_prime(2)
    True
    >>> is_prime(3)
    True
    >>> is_prime(5)
    True
    >>> is_prime(6)
    False
    >>> is_prime(10)
    True
    >>> is_prime(100)
    True
    """
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5):
        if n % i == 0:
            return False
    return True
``` 
This code defines a `prime_fib` function that calculates the n-th Fibonacci number that is prime and tests it with some code. It also has a function `is_prime` that checks if a given number is prime or not.