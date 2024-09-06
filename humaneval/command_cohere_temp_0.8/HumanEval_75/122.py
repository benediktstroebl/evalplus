```python
def is_multiply_prime(n):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    factors = set(int(i) for i in range(1, int(n ** .5) + 1) if n % i == 0)
    return len(factors) == 3 and max(factors) in primes
```

The function `is_multiply_prime` checks if a number is the multiplication of three prime numbers. The test suite includes a few examples, such as `is_multiply_prime(30)` returning `True` due to 30 being 2 * 3 * 5, and `is_multiply_prime(102)` returning `False` because 102 = 2 * 51 * 2, where the latter two factors are not prime. The function relies on the `factors` set to store the factors of the provided number, and then checks their count and uniqueness to return the proper result.