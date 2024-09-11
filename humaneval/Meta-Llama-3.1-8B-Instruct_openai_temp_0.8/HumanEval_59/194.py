### Largest Prime Factor Function
```python
def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    
    Args:
        n (int): A composite number.

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

# Example usage
print(largest_prime_factor(13195))  # 29
print(largest_prime_factor(2048))   # 2
```
This script defines a function `largest_prime_factor` that takes an integer `n` as input and returns its largest prime factor. The function iterates through all possible factors of `n`, starting from 2, and keeps dividing `n` by the factor until it is no longer divisible. The last remaining factor will be the largest prime factor of `n`. The function's time complexity is O(sqrt(n)) due to the while loop.