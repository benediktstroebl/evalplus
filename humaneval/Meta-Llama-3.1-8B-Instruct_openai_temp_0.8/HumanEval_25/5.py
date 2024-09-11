### Prime Factorization of an Integer
#### Python Function

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The number to factorize

    Returns:
    List[int]: A list of prime factors

    Example:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

# Example usage:
print(factorize(8))   # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script uses a simple trial division method to find the prime factors of a given integer. The loop starts from 2 (the smallest prime number) and checks if the current number `i` is a factor of `n`. If it is, then `n` is divided by `i`, and `i` is added to the list of factors. This process continues until `n` is reduced to 1. If `n` is greater than 1 at the end of the loop, it means that `n` itself is a prime number and is added to the list of factors.