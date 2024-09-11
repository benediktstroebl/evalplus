### Largest Prime Factor Function
#### Calculates the largest prime factor of a given number

```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
    n (int): The input number.

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

This script works by dividing the input number `n` by the smallest prime number, which is 2. If `n` is divisible by 2, it continues to divide `n` by 2 until it's no longer divisible. Then it moves on to the next prime number, which is 3, and repeats the process. This continues until the square root of `n`, as any factor larger than the square root would have a corresponding factor smaller than the square root. The remaining number `n` after this process is the largest prime factor.