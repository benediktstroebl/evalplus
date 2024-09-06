Here is a Python script that defines a self-contained function to calculate the n-th Fibonacci number that is also prime: 
```python
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_fib(n):
    """
    Returns the n-th Fibonacci number that is also prime
    >>> prime_fib(1)
    2
    >>> prime_fib(2)
    3
    >>> prime_fib(3)
    5
    >>> prime_fib(5)
    89
    """
    if n <= 1:
        return n
    if is_prime(n):
        return n
    i = 0
    while i < n - 2:
        if is_prime(i) and is_prime(n - i - 1):
            i += 1
        else:
            n -= i
    return n
```

This code defines two functions: `is_prime` checks whether a given number is prime, and `prime_fib` calculates the n-th Fibonacci number that is also prime. The `prime_fib` function uses an iterative approach with primality testing to find the prime Fibonacci number.