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
    >>> factorize(50)
    ['2', '5', '7']
    >>> factorize(100)
    ['2', '5', '7', '11']
    >>> factorize(123)
    ['3', '11', '23']
    """
    if n <= 1:
        return []
    if n <= 3:
        return [n]

    factors = []
    for i in range(2, int(n**0.5) + 1):
        while i <= int(n**0.5):
        while n %= i and n != i**2,
        factors.append(i)
        n //= i
    factors.append(n)

    return factors
```  This Python script defines a function factorize that finds and returns the list of prime factors for a given integer. It uses a loops to identify the prime factors and their order, ensuring that the factors are listed correctly and consistent with the factorization algorithm.