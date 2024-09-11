### Prime Factorization Script
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    
    Args:
        n (int): The input number to find prime factors of.

    Returns:
        List[int]: A list of prime factors of the input number.
    
    Example:
        >>> factorize(8)
        [2, 2, 2]
        >>> factorize(25)
        [5, 5]
        >>> factorize(70)
        [2, 5, 7]
    """
    factors = {}
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors[i] = factors.get(i, 0) + 1
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return [k for k, v in factors.items() for _ in range(v)]

# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script works by iteratively dividing the input number `n` by the smallest prime factor (starting from 2). If `n` is divisible by the current number `i`, it divides `n` by `i` and increments the count of `i` in the `factors` dictionary. This process repeats until `n` is reduced to 1. Finally, it constructs the list of prime factors by iterating over the `factors` dictionary and repeating each factor according to its count.