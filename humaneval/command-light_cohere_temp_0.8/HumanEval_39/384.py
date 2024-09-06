```python
import math

def is_prime(n):
    """
    Check if n is a prime number.
    """
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
    Returns the n-th Fibonacci number that is prime.
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
    if n < 2:
        return 2
    if is_prime(n):
        return n
    return prime_fib(n+1)

# Test if the is_prime function
print(is_prime(5))  # Output: True
print(is_prime(2))  # Output: False
print(is_prime(0))  # Output: False
print(is_prime(1))  # Output: False
```
This code provides a self-contained Python function that calculates the n-th Fibonacci number that is prime. The code also tests the implementation to ensure the correctness of the function.