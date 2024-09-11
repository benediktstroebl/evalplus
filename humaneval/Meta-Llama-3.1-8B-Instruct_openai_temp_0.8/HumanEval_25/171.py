### Factorize Function
#### Returns a list of prime factors of a given integer in the order from smallest to largest.

```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Returns a list of prime factors of a given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors

    Args:
        n (int): The number to factorize.

    Returns:
        List[int]: A list of prime factors of the given integer.

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
            n //= i
            factors.append(i)
        else:
            i += 1
    return factors


# Example usage:
print(factorize(8))  # Output: [2, 2, 2]
print(factorize(25))  # Output: [5, 5]
print(factorize(70))  # Output: [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` as input and returns a list of its prime factors in the order from smallest to largest. The function uses a while loop to divide the input number by the smallest divisor (starting from 2) until it is no longer divisible. The divisor is then added to the list of factors, and the division process continues until the number is reduced to 1. The function returns the list of factors.