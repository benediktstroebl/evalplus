```python
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
```

This function `is_prime(n)` returns `True` if the given number `n` is prime, and `False` otherwise. It checks if `n` is less than 2, as all prime numbers are greater than 1. It then iterates from 2 to the square root of `n` (inclusive), and for each number `i`, it checks if `n` is divisible by `i`, if so, it returns `False` as primes do not have any divisors other than 1 and themselves. If the loop completes without a divisor being found, it returns `True`, indicating that `n` is prime.