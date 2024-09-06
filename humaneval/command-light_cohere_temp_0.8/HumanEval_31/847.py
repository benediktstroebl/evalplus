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
This Python code defines a function `is_prime` that checks whether a given number `n` is a prime number. It uses a special cases for small primes and then iterates up to the square root of the number, checking for divisibility by small primes and numbers close to the square root. The function returns `True` if the number is prime, and `False` otherwise.