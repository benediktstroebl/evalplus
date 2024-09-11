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

This script uses a while loop to divide the input number `n` by the smallest divisor `i` until `n` is no longer divisible by `i`. It starts with `i = 2`, which is the smallest prime number. The loop continues until `i` is greater than the square root of `n`, because a larger factor of `n` must be a multiple of a smaller factor that has already been accounted for. Once the loop finishes, `n` is the largest prime factor of the original number.