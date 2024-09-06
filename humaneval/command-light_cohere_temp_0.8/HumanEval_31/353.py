Here is a Python script with a self-contained function that solves the problem of checking whether a given number is a prime, and passes the corresponding tests:
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

This function uses a combination of simple prime number tests and optimizations to efficiently determine whether a given number is prime or not. The function handles the and passes all tests provided in the initial prompt.