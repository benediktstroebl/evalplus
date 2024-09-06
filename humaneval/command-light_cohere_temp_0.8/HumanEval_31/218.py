Here is a self-contained Python function that checks whether a given number is prime:

```python
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
        return False
    return True
```

This function checks whether a given number `n` is prime or not. It first checks if `n` is less than or equal to 1, and if so, it returns `False` since prime numbers are greater than 1. It then iterates from 2 to the square root of `n` (inclusive) and checks if `n` is divisible by any of these numbers. If `n` has any such of these divisors, it returns `False`, indicating that `n` is not prime. If all divisors are tested and `n` isn't divisible by any of them, it returns `True`, indicating that `n` is prime.