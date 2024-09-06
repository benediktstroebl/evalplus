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

This script defines a function called `is_prime` that checks whether a given number `n` is prime or not. The function uses a simple algorithm to prime-checking, which is based on the facts that prime numbers greater than 3 are of the form 6n + 1, except 2 and 3.