```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in the order of their corresponding multiplicity in the factorization of n.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(50)
    [2, 2, 5]
    >>> factorize(100)
    [2, 2, 2, 5, 5]
    """
    # Determine all factors of n
    factors = []
    for i in range(1, int(n**0.5) + 1):
        while not n % i == 0:
            factors.append(i)
            n //= i
    factors.append(n)  # Remove last element
    factors.append(0) # Make list of factors
    return factors
```