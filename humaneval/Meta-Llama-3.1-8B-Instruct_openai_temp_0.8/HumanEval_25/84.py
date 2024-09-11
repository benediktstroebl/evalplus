```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): Input number to factorize.

    Returns:
        List[int]: List of prime factors of given number.
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
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that calculates the prime factors of a given number `n`. It iteratively divides the number by the smallest prime number (starting from 2) as long as it's divisible. If the number is not divisible by the current prime, it increments the prime number. This process continues until the number is reduced to 1. The list of prime factors is then returned.