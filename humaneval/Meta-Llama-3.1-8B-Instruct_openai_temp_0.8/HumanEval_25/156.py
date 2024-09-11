### Prime Factorization of an Integer
#### Python Script
```python
from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.

    Parameters:
    n (int): Input integer for prime factorization.

    Returns:
    List[int]: List of prime factors.

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

### Explanation

This script defines a function `factorize(n)` that takes an integer `n` and returns a list of its prime factors. The function uses a while loop to divide `n` by the smallest divisor `i` (starting from 2) as long as `n` is divisible by `i`. The divisor `i` is added to the list of factors each time `n` is divided by it. The loop continues until `n` is reduced to 1. If `n` is a prime number greater than 1, it is added to the list of factors. The function returns the list of factors.