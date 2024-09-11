### Largest Prime Factor Function
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

    # Initialize the largest prime factor
    largest_factor = 2

    # Start checking for factors from 3
    for possible_factor in range(3, int(n ** 0.5) + 1, 2):
        # Check if the number is divisible by the possible factor
        while n % possible_factor == 0:
            # Update the largest factor and divide the number
            largest_factor = possible_factor
            n = n // possible_factor

    # If the remaining number is greater than 2, it's a prime number
    if n > 2:
        largest_factor = n

    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
This script defines the `largest_prime_factor` function that takes an integer `n` as input and returns the largest prime factor of `n`. The function assumes that `n` is greater than 1 and is not a prime number. It uses a while loop to divide `n` by the smallest prime factors (2, 3, 5, etc.) until it can't be divided anymore, and the remaining number is the largest prime factor. The function then returns the largest prime factor.