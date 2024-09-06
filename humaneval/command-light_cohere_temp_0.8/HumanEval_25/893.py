```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(111)
    [3, 3, 3]
    >>> factorize(333)
    Traceback (most recent call last):
      File "<stdin>", line 65:1: TypeError: 'int' object does not support item assignment
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
        n = n // i
        i += 2
    # handle remaining factors
    for num in factors:
        while n % num == 0:
            n = n // num
    factors.append(n)
    return factors
```