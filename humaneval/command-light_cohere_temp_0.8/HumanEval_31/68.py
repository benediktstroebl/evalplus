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
This code defines a function named `is_prime` that checks whether a given number `n` is prime or not. The function uses an optimized algorithm known as the Sieve of Eratosthenes to efficiently determine the primality of the number. It returns `True` if `n` is prime and `False` otherwise.