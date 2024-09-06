```python
def prime_fib(n: int):
    """
    Return the n-th number that is a Fibonacci number and is also prime.
    >>> print(prime_fib(0))
    [0]
    [0]
    >>> print(prime_fib(1))
    2
    >>> print(prime_fib(5))
    89
    >>> print(prime_fib(10))
    False
    """
    if n == 0:
        return []
    if n == 1:
        return [0]
    if n <= 3:
        return [0, 1, 2]
    if n % 2 == 0 or n % 3 == 0:
        return [0, 2]
    else:
        # Check for divisibility by prime numbers
        i = 5
        while i * i <= n:
            if n % i == 0:
                return False
            i += 6
        return True
```