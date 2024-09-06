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
The code defines a function named `is_prime` that checks whether a given number `n` is prime or not. It uses a
 Miller-Rabin primality test, which efficiently determines whether a number is prime or not, and it passes all the tests provided.