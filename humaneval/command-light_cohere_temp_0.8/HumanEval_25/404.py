```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(77)
    [7, 7]
    >>> factorize(105)
    [5, 3, 5]
    >>> factorize(1000)
    [2, 2, 2, 5, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
   
    while n > 1:
        d = 0
        while n % d == 0:
            n /= d
            factors.append(d)
        d += 1
    factors.append(n)
    return factors
```
This function takes an integer n as input and returns a list of its prime factors in descending order. It does so by checking for divisibility and factoring by squaring, iteratively. The function runs in O(n) time complexity and has a constant space complexity of O(sqrt(n)).