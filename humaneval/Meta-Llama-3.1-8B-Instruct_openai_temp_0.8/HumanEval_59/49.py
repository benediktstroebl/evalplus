### Largest Prime Factor Function
#### Python Script
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Parameters:
    n (int): Input number.

    Returns:
    int: Largest prime factor of n.

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

    max_factor = 1
    for i in range(2, int(n ** 0.5) + 1):
        while n % i == 0:
            if is_prime(i):
                max_factor = max(max_factor, i)
            n //= i
    if n > 1 and is_prime(n):
        max_factor = max(max_factor, n)
    return max_factor

# Example usage:
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This script first defines a helper function `is_prime(num)` to check if a number is prime. The main function `largest_prime_factor(n)` then iterates over possible factors of `n`, checks if they are prime using `is_prime(num)`, and updates the maximum prime factor found. Finally, it returns the largest prime factor of `n`.