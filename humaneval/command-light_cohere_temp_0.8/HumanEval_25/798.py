```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times which correspond to how many times it appears in factorization
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(49)
    [7]
    >>> factorize(81)
    [3, 3, 3]
    >>> factorize(101)
    [3, 7, 11]
    """
    if n <= 1:
        return []

    factors = []
    while n % 2 == 0:
        factors.append(2)
        n // 2
    while n % 7 == 0:
        factors.append(7)
        n // 7
    while n % 11 == 0:
        factors.append(11)
        n // 11
    while n % 13 == 0:
        factors.append(13)
        n // 13
    while n % 17 == 0:
        factors.append(17)
        n // 17
    while n % 19 == 0:
        factors.append(19)
        n // 19
    while n % 23 == 0:
        factors.append(23)
        n // 23
    while n % 29 == 0:
        factors.append(29)
        n // 29
    while n % 31 == 0:
        factors.append(31)
        n // 31
    return factors

``` 
Do you have any other questions related to Python programming or specific topics you would like to explore?