```python
def is_prime(n):
    """
    Returns True if the number is prime, False otherwise.
    >>> 6
    False
    >>> 101  True
    >>> 11  True
    >>> 13441  True
    >>> 61  True
    >>> 4   False
    >>> 1   False
    """
    if n <= 1:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
```