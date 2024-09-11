```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    :param n: The input number.
    :return: The largest prime factor of n.
    :hints: Use a loop to divide the number by increasing integers and check for primality.
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(n - 1, 1, -1):
        # Check if i is a factor of n
        if n % i == 0:
            # Check if i is prime
            if is_prime(i):
                return i

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a helper function `is_prime` to check if a number is prime. The main function `largest_prime_factor` then uses a loop to divide the input number `n` by increasing integers, starting from `n-1` and going down to 2. If `n` is divisible by `i`, and `i` is prime, it returns `i` as the largest prime factor. 

Note that this algorithm is not the most efficient for large numbers, as it checks every number up to `n-1`. A more efficient algorithm would involve prime factorization methods like the Sieve of Eratosthenes or the Pollard's rho algorithm.