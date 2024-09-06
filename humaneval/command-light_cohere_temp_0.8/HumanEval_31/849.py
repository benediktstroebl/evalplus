Here's the self-contained Python function that checks whether a number is a prime:
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

This function will check all numbers up to `n` to see if it's a prime, and returns `True` if it is a prime, and `False` otherwise.  It can be used to pass tests with the given markdown code block.