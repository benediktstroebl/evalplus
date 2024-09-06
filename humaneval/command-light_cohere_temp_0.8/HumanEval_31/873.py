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

This Python function, `is_prime`, determines whether a given number n is prime. It uses a strategy to determine primality by checking divisibility and factoring, employing an optimized approach with efficient iterations. It meets the testability and passes all the given tests!