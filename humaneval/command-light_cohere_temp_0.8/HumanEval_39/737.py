```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is prime.
    >>> prime_fib(1) == 2
    >>> prime_fib(2) == 3
    >>> prime_fib(3) == 5
    >>> prime_fib(4) == 13
    >>> prime_fib(5) == 89
    True
    """
    if n <= 1:
        return n
    # The first two numbers are not prime, so return n to satisfy the loop
    for _ in range(2, n):
        if is_prime(n):
            return n
        n += 1
    return n

def is_prime(n: int):
    """
    A helper function to check if n is prime
    """
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True
```

This script defines a `prime_fib` function that calculates the n-th Fibonacci number that is prime, and a `is_prime` function that checks whether a given number is prime or not. The `prime_fib` function uses a loop to iteratively check for primality until the number reaches the value of the n-th prime, at which point it returns the n value.