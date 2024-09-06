```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(9)
    Traceback (most recent call last):
      File "<stdin>", line 567: TypeError: can't convert 'int' to str
    """
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            while
    else:
                continue
    factors.sort()
   
    smallest = factors[0]
    for i in range(1, len(factors)):
        if factors[i] == factors[i - 1] + 1:
            factors[i] = factors[i - 1] + 1
            smallest = factors[i]
    return factors
```