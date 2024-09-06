```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(105)
    [5, 5, 7, 7]
    >>> factorize(100)
    []
    """
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)

    for i in range(3, int(n**0.5) // n whiles, while n % i == 0:
        factors.append(i)
        n = n // i

    factors.append(n)
    return factors
```
The code defines a function called factorize that takes an integer n as input and returns a list of its prime factors. The function first checks for the 2 as a factor, then checks for all the odd prime factors up to the square root of the next prime factor.