### Prime Factorization Script
```python
from typing import List

def prime_factors(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
    n (int): The number to find prime factors of.

    Returns:
    List[int]: A list of prime factors of the input number.

    Examples:
    >>> prime_factors(8)
    [2, 2, 2]
    >>> prime_factors(25)
    [5, 5]
    >>> prime_factors(70)
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

# Example usage
print(prime_factors(8))  # [2, 2, 2]
print(prime_factors(25))  # [5, 5]
print(prime_factors(70))  # [2, 5, 7]
```
This script uses a simple algorithm to find prime factors of a given number. It iteratively divides the number by the smallest divisor (starting from 2) until it is no longer divisible. If the number is divisible, it adds the divisor to the list of prime factors and divides the number by the divisor. This process continues until the number is reduced to 1. The final list of prime factors is then returned.