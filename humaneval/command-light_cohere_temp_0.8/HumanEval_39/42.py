```python
def prime_fib(n: int):
    """
    Returns n-th number that is a Fibonacci number and is also prime.
    Returns None if n < 1.
    >>> prime_fib(1)
    2
    """
    if n < 1:
        return None
    elif n == 2:
        return 2
    else:
        # Fibonacci sequence
        a = 0
        b = 1
        for _ in range(n - 2):
            c = a + b
            a = b
            b = c
        return b
```