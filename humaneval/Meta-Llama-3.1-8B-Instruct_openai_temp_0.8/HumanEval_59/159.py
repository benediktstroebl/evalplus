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
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


# Test the function
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor` that calculates the largest prime factor of a given integer `n`. It uses a while loop to iterate from 2 to the square root of `n` (inclusive), checking for divisibility at each step. If `n` is divisible by `i`, it divides `n` by `i` and continues with the next iteration. If `n` is not divisible by `i`, it increments `i` by 1. The loop continues until `i` exceeds the square root of `n`, at which point the remaining value of `n` is the largest prime factor. The function returns this value.