```python
def prime_fib(n: int):
    """
    prime_fib returns n-th number that is a Fibonacci number and it's also prime.
    >>> print(prime_fib(5))  # Output: 89
    >>> print(prime_fib(6))  # Output: 5
    >>> print(prime_fib(7))  # Output: 8
    >>> print(prime_fib(8))  # Output: 13
    >>> print(prime_fib(9))  # Output: 22
    >>> print(prime_fib(10))  # Output: 233
    >>> print(prime_fib(15))  # Output: 5848)
    """
    if n <= 1:
        return n
    if n <= 3:
        return 2
    if n % 2 == 0:
        return 3
    i = 5
    while i * i <= n:
        if n % (i + 1) == 0 or n % i == 0:
            break
        i += 6
    return i  # Return the next Fibonacci number
```