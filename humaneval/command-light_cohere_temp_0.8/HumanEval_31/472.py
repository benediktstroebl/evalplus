Here is a self-contained Python function that determines whether a given number is a prime, passing the corresponding tests:
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

This function is designed to efficiently determine whether a given number is a prime or not, using the algorithm from the above definition. It also passes all tests for various input numbers.