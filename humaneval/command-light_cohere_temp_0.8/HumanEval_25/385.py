```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factors = factorize(8)
    [2, 2, 2]
    >>> factors = factorize(25)
    [5, 5]
    >>> factors = factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
    factors.append(n)
   
    if n > 1:
        factors.append(n)
    else:
        break
    for i in range(3, int(n**0.5) //,  while n % i == 0:
        factors.append(i)
    factors.append(n)
    return factors
```

The function factors will return a list of prime factors of the given number, and the order of the factors will be from smallest to largest.