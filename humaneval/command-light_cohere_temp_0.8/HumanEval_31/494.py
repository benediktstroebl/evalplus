Here's the self-contained Python function:
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
This function, `is_prime`, takes an integer `n` as input and returns `True` if `n` is a prime number, and `False` otherwise. It uses a for checking primality, following the `Sieve of Eratosthenes` algorithm, which is efficient for larger numbers. 

Please note that this function is self-contained and can be used to solve the problem and pass all the corresponding tests without needing external code.