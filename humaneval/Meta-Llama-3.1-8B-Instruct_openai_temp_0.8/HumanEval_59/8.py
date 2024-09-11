```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): A number greater than 1.

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

    # Start checking from 2, the smallest prime number
    i = 2

    # Continue checking until we reach the square root of n
    while i * i <= n:
        # If n is divisible by i, it means i is a factor of n
        if n % i:
            # If n is not divisible by i, increment i by 1
            i += 1
        else:
            # If n is divisible by i, update the largest factor
            n //= i
            largest_factor = i

    # At this point, n is a prime number greater than its square root
    # So, it's the largest prime factor
    if n > largest_factor:
        largest_factor = n

    return largest_factor

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function uses a while loop to iterate through numbers from 2 to the square root of `n`, checking if each number is a factor of `n`. If it is, the function updates the largest factor and divides `n` by the factor. At the end of the loop, `n` is a prime number, so it's the largest prime factor of the original `n`. The script then tests the function with the provided examples.