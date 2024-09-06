```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(91)
    [3, 7, 7]
    >>> factorize(49)
    [7, 3, 3]
    """
    factors = []
    while n % 2 == 0:
        n = n / 2
        factors.append(n)
   
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n / i
    factors.append(n)
    return factors
```

This script defines a function called `factorize` that calculates the prime factors of a given number. It uses a list comprehension to find all factors of a given number and lists them in order of decreasing magnitude. 

The function can be used to find the prime factors of any positive integer.