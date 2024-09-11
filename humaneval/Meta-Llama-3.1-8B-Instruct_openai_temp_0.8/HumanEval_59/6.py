### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): Input number.

    Returns:
    int: The largest prime factor of n.

    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Initialize the largest factor to 1
    largest_factor = 1

    # Start from the smallest prime factor, 2
    i = 2

    # Continue the loop until the number n is reduced to 1
    while n > 1:
        # If n is divisible by i, then i is a factor of n
        if n % i == 0:
            # Update the largest factor if i is larger
            largest_factor = max(largest_factor, i)
            # Divide n by i to remove this factor from n
            n = n // i
        else:
            # If i is not a factor, increment it by 1
            i += 1

    # Return the largest prime factor
    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function uses a loop to find all the prime factors of `n`, keeping track of the largest one found. It starts from the smallest prime factor, 2, and increments the potential factor by 1 each time a factor is found, until `n` is reduced to 1.