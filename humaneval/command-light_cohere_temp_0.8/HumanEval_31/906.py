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
This function, `is_prime`, checks whether a given number `n` is prime or not. It uses the process to repeatedly check divisibility up to the square root of `n`, and returns `True` if `n` is prime and `False` otherwise.