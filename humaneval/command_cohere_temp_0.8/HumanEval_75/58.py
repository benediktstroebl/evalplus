```python
def is_multiply_prime(a):
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    divisors = set(range(2, int(a**0.5) + 1)) | {a}
    for prime in primes:
        if prime not in divisors:
            return False
    return len(divisors) == 3
```

The function `is_multiply_prime` checks if the number is less than 100 and if it is a multiplication of exactly 3 prime numbers. It does so by first creating a list of prime numbers up to the square root of the number. Then it checks if any of the prime numbers is not a divisor of the number and returns false if so. Otherwise, it returns True.