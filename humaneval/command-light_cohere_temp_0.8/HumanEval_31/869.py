Here is a Python script with a self-contained function that solves the problem of checking whether a given number is a prime, and passes the corresponding tests:

```python
def is_prime(n):
    """Return true if a given number is prime, and false otherwise."""
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

This code defines a function `is_prime` that checks whether a given number `n` is a prime number or not. The function first handles special cases where `n` is less than or equal to 1, as these numbers are not prime. Then, it checks for divisibility by 2 and 3, returning `False` if `n` is divisible by either of these numbers. The function then starts a loop from 5 (the first odd number) and checks for divisibility by numbers in the form of `i^2 + 6k`, where `k` is any integer less than or equal to 5. The loop continues until `i * i` exceeds the given number `n`, and if any such divisors are found, the function returns `False`.  If no divisors are found, the function returns `True`.