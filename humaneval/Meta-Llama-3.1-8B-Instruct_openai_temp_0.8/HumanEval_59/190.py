### Largest Prime Factor
#### Problem Statement
Find the largest prime factor of a given integer `n`.

#### Solution
```python
def largest_prime_factor(n: int) -> int:
    """
    Return the largest prime factor of n. Assume n > 1 and is not a prime.

    Args:
        n (int): An integer greater than 1.

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
print(largest_prime_factor(600851475143))  # Output: 6857
```

This script uses a simple algorithm to find the largest prime factor of a given integer `n`. The algorithm works by dividing `n` by the smallest prime number `i` (starting from 2) as long as `n` is divisible by `i`. The process continues until `n` is no longer divisible by `i`. The remaining value of `n` is the largest prime factor.

This solution is efficient because it only checks divisibility up to the square root of `n`, reducing the number of iterations.