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
This function, named `is_prime`, takes an integer `n` as an argument and checks whether `n` is a prime number or not. It uses some basic algorithms to achieve this, such as the `sqrt_prime` and the Sieve of Eratosthenes.