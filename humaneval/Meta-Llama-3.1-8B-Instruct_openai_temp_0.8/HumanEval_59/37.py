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
print(largest_prime_factor(13195))  # Outputs: 29
print(largest_prime_factor(2048))   # Outputs: 2
```

This script defines a function `largest_prime_factor(n)` that calculates the largest prime factor of a given number `n`. It starts by checking divisibility from 2 and increments the divisor until it finds a number that is not divisible by any of the previous numbers. This process continues until the remaining number `n` is a prime number, which is then returned as the largest prime factor. The time complexity of this algorithm is O(sqrt(n)), which is efficient for calculating the largest prime factor of a number.