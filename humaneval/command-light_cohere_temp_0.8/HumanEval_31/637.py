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
The function `is_prime` in the above code takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. It uses a
 classic Sieve of Eratosthenes algorithm to determine primality.