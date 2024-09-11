```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    :param n: An integer greater than 1 and not a prime.
    :return: The largest prime factor of n.
    """
    def is_prime(num: int) -> bool:
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_factor = None
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_factor = i
    return largest_factor


# Test cases
if __name__ == "__main__":
    print(largest_prime_factor(13195))  # Output: 29
    print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that finds the largest prime factor of a given integer `n`. It uses a helper function `is_prime` to check if a number is prime. The main function iterates from 2 to `n` (inclusive), checks if each number is a factor of `n` and a prime number, and keeps track of the largest prime factor found.

Note: This script uses a trial division approach to check for prime numbers, which is not the most efficient method for large numbers. For a more efficient solution, consider using the Sieve of Eratosthenes algorithm or a probabilistic primality test.