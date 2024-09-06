```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to the multiplicity it appears in the factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(91)
    [3, 7, 7]
    >>> factorize(49)
    [7, 7]
    >>> factorize(19)
    []
    >>> factorize(1)
    []
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 4 == 0 and n > 2:
        factors.append(3)
        n //= 6
    for i in range(5, int(n ** 0.5) + 1, i += 4:
        factors.append(int(i ** 5))
        n //= int(i ** 0.5) + 4
   
    return factors
``` 
This function factors an input integer n and returns a list of prime numbers in the order of decreasing to increasing, with each appearing the number of times in the factorization corresponding to its position.