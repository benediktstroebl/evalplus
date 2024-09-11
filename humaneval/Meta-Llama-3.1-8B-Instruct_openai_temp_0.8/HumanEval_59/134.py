### Largest Prime Factor of a Number
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): A positive integer greater than 1.

    Returns:
    int: The largest prime factor of n.

    Example:
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # Start checking from 2, which is the smallest prime number
    i = 2
    # Continue checking until i is less than or equal to the square root of n
    while i * i <= n:
        # If n is divisible by i, then i is a prime factor of n
        if n % i:
            # If n is not divisible by i, then increment i by 1
            i += 1
        else:
            # If n is divisible by i, then n = n / i
            n = n // i
    # At this point, n itself is a prime factor of the original number
    return n

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```
In this code, we start checking from 2 and continue checking until the square root of `n`. If `n` is divisible by `i`, then we divide `n` by `i` and continue checking with the new value of `n`. If `n` is not divisible by `i`, then we increment `i` by 1. This process is repeated until `i` is greater than the square root of `n`. At this point, `n` itself is a prime factor of the original number.