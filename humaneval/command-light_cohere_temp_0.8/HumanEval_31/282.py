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

This code checks whether a given number `n` is prime or not. It employs a specific tests and a simple heuristic to iterate through numbers and test for divisibility up to the square root of the number. The function returns `True` if the number is prime and `False` otherwise.