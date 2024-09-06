```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(110)
    [2, 5, 10, 2]
    """
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
    while n % 3 == 0:
        n = n // 3
        factors.append(3)
    while n % 5 == 0:
        n = n // 5
        factors.append(5)
    while n % 7 == 0:
        n = n // 7
        factors.append(7)
    while n % 11 == 0:
        n = n // 11
        factors.append(11)
    while n % 13 == 0:
        n = n // 13
        factors.append(13)
    while n % 17 == 0:
        n = n // 17
        factors.append(17)
    while n % 19 == 0:
        n = n // 19
        factors.append(19)
    while n % 23 == 0:
        n = n // 23
        factors.append(23)
    while n % 29 == 0:
        n = n // 29
        factors.append(29)
    while n % 31 == 0:
        n = n // 31
        factors.append(31)
    return factors
```
The function first initializes an empty list to store the prime factors. It then enters a loop, which continues until the number is even (i. From there, it checks for divisibility by 2, 3, 5, 7, and 11, and adds the corresponding prime factors to the list. If the number is odd after the loop exits, it has completed the factorization and returns the list of prime factors.