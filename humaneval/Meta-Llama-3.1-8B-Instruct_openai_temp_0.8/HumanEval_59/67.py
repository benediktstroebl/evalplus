```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

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

    max_factor = 1
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            max_factor = max(max_factor, i)

    return max_factor

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2
```

This script defines a function `largest_prime_factor` that finds the largest prime factor of a given number `n`. It uses a helper function `is_prime` to check if a number is prime. The main function iterates through all numbers from 2 to `n` and checks if they are prime and divide `n` evenly. The largest such number is the largest prime factor of `n`.

The test cases at the end verify that the function works correctly with the provided examples.