```python
def is_prime(n):
    """Check if a number is prime"""
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_up_to(n):
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n."""
    count = 0
    primes = []
    for i in range(2, n + 1):
        if is_prime(i) and i < n:
            primes.append(i)
            count += 1
            if count == n:
                break
    return primes
```

This script defines a `count_up_to` function that solves the problem as outlined using a simple `is_prime` function to check if a number is prime. This approach is efficient and can easily handle the test cases provided in a fraction of a second, as the largest number to be checked for primality in the test cases is only 19. It should be noted that for larger values of `n`, this method may not be very efficient, due to the larger time complexity of the `is_prime` function. Other more efficient techniques for checking primality like the Sieve of Eratosthenes could be used if needed.  If efficiency is not concern, the provided solution is a simple and straightforward way of solving the problem.