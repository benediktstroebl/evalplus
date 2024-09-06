```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the same number of times in factorization corresponding to their position in the list.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(77)
    [7, 7]
    >>> factorize(360)
    [2, 2, 2, 3, 3, 5, 5, 3]
    >>> factorize(243)
    [3, 3, 3]
    """
    factors = []
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            factors.append(i)
            while n/=i
    factors.append(n)
    return factors
    ```