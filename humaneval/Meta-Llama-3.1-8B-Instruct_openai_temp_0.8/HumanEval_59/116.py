```python
def largest_prime_factor(n: int):
    """
    Return the largest prime factor of n.
    Assume n > 1 and is not a prime.

    Args:
        n (int): The number to find the largest prime factor for.

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
print(largest_prime_factor(2048))   # Output: 2
```

This script defines a function `largest_prime_factor(n)` that takes an integer `n` as input and returns its largest prime factor. The function uses a while loop to check for divisibility from 2 to the square root of `n`, and returns the remaining number after the loop, which is guaranteed to be a prime number. The script also includes test cases to demonstrate the function's correctness.