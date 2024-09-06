```python
def prime_fib(n: int):
    """
    Returns the n-th number that is a Fibonacci number and is also prime.
    >>> print(prime_fib(6))
    3
    """
    if n <= 1:
        return n
    if n == 2:
        return 2
    if n % 2 == 0:
        return False

    # Check primality using division method
    temp = prime_fib(mod_pow(2, n - 1, n))
    return temp != temp + 1
```