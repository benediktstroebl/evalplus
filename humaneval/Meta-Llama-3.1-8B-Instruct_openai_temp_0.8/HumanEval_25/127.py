### Prime Factorization Script
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

    Examples:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    i = 2
    while n > 1:
        if n % i == 0:
            count = 0
            while n % i == 0:
                n = n // i
                count += 1
            factors.extend([i] * count)
        i += 1
    return factors

# Test the function
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```
This script defines a function `factorize` that calculates the prime factors of a given integer `n`. It uses a simple iterative approach, starting from the smallest prime number (2) and checking if `n` is divisible by it. If it is, it adds the divisor to the list of factors and divides `n` by the divisor as many times as possible. This process continues until `n` is reduced to 1. The function returns the list of prime factors.