```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return not any(factor in factors for prime in primes for factor in primes if prime ** 3 > factors[factor] > 0)
```

The function `is_multiply_prime` checks if a given number is the product of three prime numbers. It first collects the prime factors of the number, and then it iterates over all the primes up to the square root of the number and checks if each one of them is a factor or not. If there are no common factors for all primes other than 1, the number is returned as a product of three primes.