### Largest Prime Factor Function
```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): A positive integer.

    Returns:
        int: The largest prime factor of n.

    Examples:
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

    largest_factor = None
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            largest_factor = i
    return largest_factor
```
### Example Usage
```python
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It uses a helper function `is_prime` to check if a number is prime. The `largest_prime_factor` function iterates from 2 to `n` (inclusive) and checks if each number is a factor of `n` and a prime number. If it finds such a number, it stores it as the largest factor and returns it at the end.