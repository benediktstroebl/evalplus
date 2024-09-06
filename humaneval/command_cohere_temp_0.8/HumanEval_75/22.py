```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, a + 1) if a % i == 0)
    return not any(factor in factors for prime in primes for factor in primes if prime ** 2 > a)
```

The function `is_multiply_prime` checks if the given number is the product of three prime numbers. It first suspects all the possible factors of the given number and then checks if any combination of primes could yield the suspect factors. It does so by looping over all primes and for each prime suspecting if there is a combination of two primes that would yield the suspect factor. If there is no such pair for any of the factors, then the suspicion is true.