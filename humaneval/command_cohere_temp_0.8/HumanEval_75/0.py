```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return not any(x in factors for x in primes)
```

The function `is_multiply_prime` checks if a given number is the multiplication of three prime numbers. It first generates a list of prime numbers up to `100`. Then it checks all possible factors of the given number `n` and verifies if any of them is a prime number. If this is the case, the function returns `False`. Otherwise, it returns `True`.