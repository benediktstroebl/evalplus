```python
def is_prime(n):
    """Returns true if the number is prime, and false otherwise."""
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

This Python function checks whether a given number is prime or not. It uses the simple and efficient algorithm to solve this problem. The function starts by handling the cases where the number is less than or equal to one, then checks for the number being divisible by 2 or 3, and then, it uses a simple trial and error algorithm to check for primality up to the square root of the number.