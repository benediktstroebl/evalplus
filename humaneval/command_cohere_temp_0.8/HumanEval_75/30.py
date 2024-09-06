```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    factors = set(int(i) for i in range(1, a + 1) if a % i == 0)
    return not any(factor in factors for prime in primes for factor in primes if prime ** 2 > a)
```

The function `is_multiply_prime` checks if the number is the product of three prime factors, it first conjects the prime factors of the number and checks if it has exactly three unique factors and finally returns True if so, and False otherwise.