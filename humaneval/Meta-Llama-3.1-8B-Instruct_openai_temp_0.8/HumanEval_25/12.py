### Prime Factorization Script
```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.

    Args:
        n (int): Input number

    Returns:
        List[int]: List of prime factors

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
This script utilizes a simple trial division method to find prime factors. It starts with the smallest prime number (2) and divides the input number `n` by it as long as possible. If `n` is not divisible by the current number `i`, it increments `i` by 1. The process continues until `n` is reduced to 1. The list of prime factors is constructed by appending each factor to the list as many times as it appears in the factorization.