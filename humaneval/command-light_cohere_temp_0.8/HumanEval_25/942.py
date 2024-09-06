```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, corresponding to how many times it appears in the factorization of n.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # Create list to store prime factors
    factors = []

    # Loop through 1 to the square root of n
    i = 2
    while i*i <= n:
        # Check if i is a factor of n
        if n % i == 0:
            factors.append(i)
            # Add i to the factorization list
            factors.append(i * )
        i += 1

    # If n is a prime, add n to the list
    if n != 1:
        factors.append(n)

    # Return list of prime factors
    return factors
```