```python
def largest_prime_factor(n):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime."""
    def is_prime(m):
        """Check if m is a prime number."""
        if m < 2:
            return False
        for i in range(2, int(m**0.5) + 1):
            if m % i == 0:
                return False
        return True

    for i in range(2, n):
        if n % i == 0 and is_prime(i):
            return i
    return n
```

The function `largest_prime_factor(n)` takes a number `n` as input and returns the largest prime factor of `n`. It starts with a helper function, `is_prime(m)`, which checks if a number `m` is prime. Initially, it checks if `m` is smaller than 2, returning False instantly in such a case. It then loops through numbers from 2 to the square root of `m`, checking if `m` is divisible by any of them. If there are no divisors, it returns True, signifying that `m` is a prime number.

The main function iterates through numbers from 2 to `n`, checking if `n` is divisible by each number and if the divisor is prime. It returns the largest such prime divisor, assuming that `n` is not a prime itself. This approach efficiently identifies the largest prime factor without the need for complex prime-finding algorithms.