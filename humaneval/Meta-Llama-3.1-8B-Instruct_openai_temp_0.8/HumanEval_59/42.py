```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """
    def is_prime(num: int) -> bool:
        """Check if num is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    max_factor = 1
    i = 2
    while n > 1:
        if n % i == 0 and is_prime(i):
            max_factor = i
            n //= i
        else:
            i += 1
    return max_factor

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses the `is_prime` helper function to check if a number is prime. The main `largest_prime_factor` function then iterates over numbers from 2 to `n` (inclusive) to find the largest prime factor. If `i` is a prime number and a divisor of `n`, it updates `max_factor` and divides `n` by `i`. The loop continues until `n` is reduced to 1.