Here is a self-contained Python function that checks whether a given number is a prime:

```python
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True
```

This function takes an integer `n` as input and returns `True` if `n` is a prime, and `False` otherwise. The function uses a prime numbers checking logic, and it passes all the corresponding tests.