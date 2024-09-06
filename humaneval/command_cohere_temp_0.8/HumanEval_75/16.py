```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = [val for val in primes if n % val == 0]
    return len(divisors) == 3
```

The function `is_multiply_prime` checks if the number n is the multiplication of 3 prime numbers. It does so by first assuming that n is multiply prime, it tries to find three primes that fit the criteria. If it succeeds in finding these three primes, it returns True, otherwise, it returns False.