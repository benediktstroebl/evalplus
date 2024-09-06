Here is a Python script that solves the problem of checking whether a given number is a prime, and passes the corresponding tests:

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

This function checks whether a given number `n` is prime or not. It first handles the basic cases, then performs a series of iterations to remove all factors less than or equal to the square root of `n`. The function returns `True` if `n` is a prime number, and `False` otherwise.