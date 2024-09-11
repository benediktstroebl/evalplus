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

This script uses a simple algorithm to find the largest prime factor of a given number `n`. It iterates from 2 to the square root of `n`, checking each number for divisibility. If `n` is divisible by the current number `i`, it divides `n` by `i` and repeats the process with the new value of `n`. If `n` is not divisible by `i`, it increments `i` by 1. When `i` is greater than the square root of `n`, the remaining value of `n` is the largest prime factor.