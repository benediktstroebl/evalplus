```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    >>> print(prime_fib(5))
    2
    3
    5
    """
    if n <= 1:
        return n
    if n % 2 == 0:
        return prime_fib(n - 2)
    for i in range(3, n + 1, 2):
        if prime_fib(i) == True:
            return i
```