```python
def largest_prime_factor(n: int):
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

    def is_prime(num):
        """Check if a number is prime."""
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Start from the largest possible factor (n / 2)
    for i in range(n // 2, 1, -1):
        # Check if the factor is a prime number and a divisor of n
        if is_prime(i) and n % i == 0:
            return i

    # If no prime factor is found, the number itself is prime
    return n


# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a helper function `is_prime` to check whether a number is prime or not. It then starts from the largest possible factor (`n / 2`) and checks each number to see if it is a prime number and a divisor of `n`. The first such number it finds is the largest prime factor. If no prime factor is found, it means the number itself is prime, so it returns the number itself.