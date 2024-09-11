```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): The input number.

    Returns:
        int: The largest prime factor of n.

    Example:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_prime = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            max_prime = max(max_prime, i)
    return max_prime

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor(n)` that takes an integer `n` as input and returns its largest prime factor. The function uses a helper function `is_prime(num)` to check if a number is prime. It iterates over all numbers from 2 to `n` and checks if they are divisible by `n` and if they are prime. The largest prime factor found is returned.

Please note that this script uses a naive approach to find the largest prime factor, which may not be efficient for large numbers. A more efficient approach would be to use the Sieve of Eratosthenes algorithm to find all prime numbers up to `n` and then check their divisors.