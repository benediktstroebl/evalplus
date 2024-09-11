```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
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
print(factorize(8))   # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```

This script defines a function `factorize` that takes an integer `n` and returns a list of its prime factors in ascending order. The function works by dividing the input number `n` by the smallest divisor `i` (starting from 2) as long as it's divisible. The divisor `i` is then added to the list of factors, and the process is repeated until `n` is reduced to 1. If `n` is a prime number greater than 1 at the end of the loop, it's added to the list of factors. The function returns the list of factors.

The example usage at the end of the script demonstrates how to use the `factorize` function with different inputs.