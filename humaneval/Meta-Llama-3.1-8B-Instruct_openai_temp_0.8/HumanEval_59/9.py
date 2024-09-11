```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): A number greater than 1 that is not a prime.

    Returns:
        int: The largest prime factor of n.

    Examples:
        >>> largest_prime_factor(13195)
        29
        >>> largest_prime_factor(2048)
        2
    """
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))  # Output: 2
```

This script defines the `largest_prime_factor` function, which finds the largest prime factor of a given number `n`. It uses a while loop to divide `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. The loop continues until `n` is a prime number, and the function returns `n` as the largest prime factor. The test cases at the end demonstrate the function's correctness.