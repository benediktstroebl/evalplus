```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all the factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(50)
    [2, 2, 5, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 5, 10, 2]
    """
    # Using the sieve of Eratosthenes to find prime factors
    factors: List[int] = []
    for i in range(2, int(n**0.5)):
        if n % i == i: factors.add(i)
   
    n = n // i
    return factors
```