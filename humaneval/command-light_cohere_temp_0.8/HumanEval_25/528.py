```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(111)
    [3, 3, 3]
    >>> factorize(360)
    [2, 2, 2, 3, 3, 3, 6]
    """
    # initialize a list to store prime factors
    factors = []

    # loop to find factors of number
    for i in range(1, int(n**0.5) + 1):
        # check if divisible by i
        while n % i == 0:
            factors.append(i)
            n //=i
        while n % i == 0 and i != factors[-1]:
            factors.append(i)
            n //=i

    # return list of prime factors
    return factors
```