Here's a Python script with a self-contained function `is_prime` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function adheres to the given test cases and returns `True` for prime numbers and `False` for non-prime numbers. It handles edge cases like 1 and composite numbers like 6 and 61. The `range` function is used to iterate up to `n`'s square root to efficiently rule out potential divisors.