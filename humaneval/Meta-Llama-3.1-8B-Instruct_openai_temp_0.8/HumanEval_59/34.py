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

    # Initialize the largest factor as 2 (the smallest prime number)
    largest_factor = 2

    # Loop from 2 to the square root of n
    for i in range(2, int(n ** 0.5) + 1):
        # Check if i is a factor of n
        while n % i == 0:
            # Update the largest factor
            largest_factor = i
            # Divide n by i
            n = n // i

    # If n is a prime number greater than 2, it is the largest factor
    if n > 2:
        largest_factor = n

    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. It iteratively divides `n` by the smallest prime numbers (2, 3, 5, etc.) until it cannot be divided further. The last non-1 divisor is the largest prime factor. If `n` is a prime number greater than 2, it is the largest factor.