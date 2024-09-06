```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest. The factors are listed according to the number of times they appear in factorization.
    Input number should be equal to the product of all factors.
    """ example:
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    for i in range(1,int(n**.5)+1):
        if n%i == 0:
            factors.append(i)
            n = n//i
    if n > 2:
        factors.append(n)
    return factors
```

This script defines a function `factorize` which accepts an integer `n` as an argument and returns a list of prime factors of the input integer `n` in the order of their occurrence in factorization. The function uses a iterative approach to finding the prime factors and checks for divisibility before adding a factor to the list of factors.

The output will be a list of prime factors.