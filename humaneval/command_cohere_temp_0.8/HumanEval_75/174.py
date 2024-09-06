```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return not any(x in factors for x in primes)
```

The function `is_multiply_prime(n)` takes a number `n` as input and checks it against a predefined list of prime numbers. It then calculates the factors of `n` up to its square root, and checks if any of these factors are in the list of primes. If there are no shared factors, the function returns `True`, and if any prime factors are found, it returns `False`. The code employs a set data structure to efficiently check for membership without the need for multiple iterations.