```python
def prime_fib(n: int):
    if n <= 1:
        return n
    if n <= 3:
        return 3
    if n % 2 == 0 or n % 3 == 0:
        return 5
    # Compute prime factorization and find next prime using the next_prime function
    factors = prime_factors(n)
    next_prime = next(factors)
    return next_prime + 1  # return the next Fibonacci number

def prime_factors(n: int):
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(n // 2)
        n = n // 2
    while n > 1:
        if n % 2 == 0:
            factors.append(n)
            n = n // 2
        elif n % 3 == 0:
            factors.append(n)
            n = n // 3
        else:
            i = 4
            while i <= int(n ** 0.5):
                factors.append(i)
                i += 6
    return factors
```

This script defines a function `prime_fib` that calculates the n-th Fibonacci number that is prime and returns the n+1. It also defines a function `prime_factors` that calculates the prime factorization of a given number n, and then uses this function to find the next prime number.