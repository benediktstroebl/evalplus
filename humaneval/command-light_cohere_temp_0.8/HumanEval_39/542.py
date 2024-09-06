```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    >>> print(prime_fib(5))  # Output: 89
    >>> is_prime(89)
    True
    >>> is_prime(0)
    False
    >>> is_prime(10)
    False
    >>> is_prime(21)
    True
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    # Check if n is a prime number using a loop
    is_prime = False
    for i in range(2, n + 1):
        if is_prime and (n % i) == 0:
            return False
        is_prime = True if n % i == 0 else False
    return True
```