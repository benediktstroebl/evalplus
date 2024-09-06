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

This code defines a function called `is_prime` that checks whether a given number `n` is prime or not. It uses a specific conditions and trial-and-error methods to determine primality. The function passes all test cases and returns `True` for prime numbers and `False` for non-prime numbers.