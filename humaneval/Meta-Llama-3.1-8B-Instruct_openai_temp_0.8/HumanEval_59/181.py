```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): A number greater than 1.

    Returns:
        int: The largest prime factor of n.

    Examples:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    # Initialize the largest factor to 2 (smallest prime number)
    largest_factor = 2

    # Check all numbers up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        # If i is a factor of n
        while n % i == 0:
            # Update the largest factor if i is larger
            largest_factor = max(largest_factor, i)
            # Divide n by i to check other factors
            n = n // i

    # If n is a prime number greater than 2
    if n > 2:
        # Update the largest factor
        largest_factor = n

    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses a simple trial division method to find the largest prime factor of a given number `n`. It starts by checking all numbers up to the square root of `n` to see if they are factors of `n`, and updates the largest factor as it finds larger ones. If `n` itself is a prime number greater than 2, it is updated as the largest factor. The function then returns the largest prime factor found.