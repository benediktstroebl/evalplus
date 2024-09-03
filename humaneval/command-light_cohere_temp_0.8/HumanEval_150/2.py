```python
def is_prime(n):
    """Check whether n is a prime number or not"""
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

def x_or_y(n, x, y):
    """Returns the value of x if n is a prime number, else returns y"""
    return is_prime(n) and x else y
```
Do you need anything else?