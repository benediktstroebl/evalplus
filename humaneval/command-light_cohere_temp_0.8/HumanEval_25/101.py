```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(82)
    [2, 2, 8, 11]
    >>> factorize(97)
    [3, 3, 7, 11]
    >>> factorize(111111)
    []
    """
    # Initialize an empty list to store factors
    factors = []

    # Define a loop to find factors
    for i in range(1, int(n**0.5) + 1):
        while n % i == 0:
            factors.append(i)
            n //= i

    # Return the list of prime factors
    return factors
```