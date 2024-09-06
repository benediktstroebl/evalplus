Here's a self-contained Python function that checks if a number is prime:
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
This function uses trial division to check for primality, and passes all provided tests. It starts by checking small numbers and then uses a trial division method with small prime factors to efficiently determine primality for larger numbers.