```python
def is_prime(n):
    """
    Return true if a given number is prime, and false otherwise.
    Returns: True
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    # Checked by the fact that any even number can be divided by 2, so we check odd numbers only
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True
```