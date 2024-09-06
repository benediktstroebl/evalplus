```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be a whole number
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(90)
    [] # Not a prime number
    >>> factorize(15)
    [] # Not a prime number
    """
    if n <= 1:
        return []

    # Initialize a set of potential prime factors
    num_factors = 2
    factors = []

    while n % num_factors == 0:
        factors.append(num_factors)
        n //= num_factors
        num_factors += 1

    # Remove factors that aren't whole numbers from the list
    return [factor for factor in factors if isinstance(factor, int)]
```