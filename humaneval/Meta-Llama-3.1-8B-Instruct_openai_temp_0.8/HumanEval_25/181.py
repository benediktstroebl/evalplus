### Prime Factorization Script
```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.

    Args:
    n (int): The input integer to be factorized.

    Returns:
    List[int]: A list of prime factors of the input integer.

    Example:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            n = n // divisor
            factors.append(divisor)
        else:
            divisor += 1

    return factors

# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```
This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function works by continuously dividing the input number by the smallest divisor (starting from 2) until it is no longer divisible. The divisor is then incremented until it finds the next number that can divide the input number. This process is repeated until the input number is reduced to 1. The list of divisors used in the process is then returned as the list of prime factors.