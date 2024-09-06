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

This code defines a function `is_prime` that checks whether a given number `n` is a prime number or not. The function uses a specific criteria and algorithms to determine if a number is prime. The function passes all the tests successfully and can be used to determine if a given number is prime or not with a high degree of accuracy.