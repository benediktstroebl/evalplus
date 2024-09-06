Here's a Python script with a self-contained function `is_prime(n)` that solves the problem:
```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function checks if a given number is prime or not. It first checks if the number is less than 2, returning `False` if so. Then, it iterates from 2 to the square root of the number, checking for divisibility. If the number is divisible by any integer in that range, it returns `False`. If neither condition is met, it returns `True`.

This implementation provides a straightforward solution to the problem in a self-contained manner, as it doesn't rely on any external libraries or functions.