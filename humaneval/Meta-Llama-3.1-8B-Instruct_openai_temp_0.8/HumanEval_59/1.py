```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. 
    Assume n > 1 and is not a prime.

    Args:
    n (int): A number greater than 1 that is not a prime.

    Returns:
    int: The largest prime factor of n.
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

This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function iterates from 2 to the square root of `n`, checking if `n` is divisible by the current number. If it is, it divides `n` by the current number and continues checking. Once `n` is no longer divisible by any number up to its square root, it means `n` itself is a prime number and is thus the largest prime factor.