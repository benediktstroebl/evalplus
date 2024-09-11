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
        while n % i == 0:
            factors.append(i)
            n = n // i
        i += 1
    return factors


# Test the function
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize(n)` that takes an integer `n` as input and returns a list of its prime factors. The function works by repeatedly dividing `n` by the smallest divisor `i` (starting from 2) until `n` is no longer divisible by `i`. The divisor `i` is then added to the list of factors, and `n` is updated to be the quotient of `n` divided by `i`. This process continues until `n` is reduced to 1. Finally, the list of factors is returned.