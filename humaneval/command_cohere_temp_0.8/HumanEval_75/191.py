```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return not any(p in factors for p in primes)
```

The function `is_multiply_prime` checks if a given number is the multiplication of three prime numbers. It first calculates the factors of the input number `n` and then checks if any of these factors are primes. If there are no shared factors it returns `True`, else `False`.