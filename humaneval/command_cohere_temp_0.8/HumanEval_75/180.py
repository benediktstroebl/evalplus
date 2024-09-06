```python
def is_multiply_prime(a):
    prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    if a < 100 and a > 1:
        divisors = []
        for prime in prime_numbers:
            if a % prime == 0:
                divisors.append(prime)
        if len(divisors) == 3:
            return True
    return False
```

This Python code defines a function called `is_multiply_prime(a)` that checks whether the given number `a` is the product of exactly three prime numbers. The function first defines a list of prime numbers up to the square root of `a` (locale-dependent primality testing). It then iterates through these prime numbers, checking for divisibility by each prime. If the number `a` is divisible by exactly three different primes, it returns `True`, indicating that the number is the product of three prime numbers. Otherwise, it returns `False`.