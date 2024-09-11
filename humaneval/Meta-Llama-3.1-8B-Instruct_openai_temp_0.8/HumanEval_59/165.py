### Largest Prime Factor Function

The following Python script defines a function `largest_prime_factor` that finds the largest prime factor of a given number `n`.

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

# Test cases
print(largest_prime_factor(13195))  # Output: 29
print(largest_prime_factor(2048))   # Output: 2
```

This script uses the property that a larger factor of the number must be a multiple of a smaller factor that has already been checked. It starts checking from the smallest prime number, 2, and increases the divisor until it finds a factor. Once a factor is found, it divides the number by the factor as many times as possible and continues checking the remaining number. If no factors are found, the remaining number itself is the largest prime factor.