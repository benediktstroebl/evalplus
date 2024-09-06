```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** 0.5) + 1) if n % i == 0)
    return len(factors) == 3 and factors & set(primes) == factors
```
The function `is_multiply_prime` checks if the number `n` is the product of three prime numbers. It first creates a list of prime numbers up to `n` and then calculates all the factors of `n`, checking if their number is exactly three and that all these factors are present in the prime number list.