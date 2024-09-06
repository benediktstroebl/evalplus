```python
def prime_fib(n: int):
    """
    This function returns the n-th number that is a Fibonacci number and is also prime.
    Returns None if n is not a positive integer.
    """
    if not isinstance(n, int) or n <= 0:
        return None
    # 0 is not a prime number
    if n == 0:
        return 1
    # Check if n is 2 or 3
    if n == 2 or n == 3:
        return n
    # Check if n is a prime number using a primality test
    n_prime = n + 1
    if all(all(x <= 1 for x in (2, 3, n_prime + 1))):
        return n
    else:
        return None
```