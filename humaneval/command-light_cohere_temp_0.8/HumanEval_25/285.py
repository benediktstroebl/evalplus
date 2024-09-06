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
    >>> factorize(49)
    []
    >>> factorize(0)
    []
    >>> factorize(10)
    [1]
    >>> factorize(900)
    []
    """
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
        yield i
    else:
        yield from factorize(n//i)
```
The function factorize takes an integer n as input and returns a list of prime factors of the number in ascending order. Each factor is provided the in order of occurrence, since a factor will be a prime if and only if it appears in each factorization for a given number exactly once.