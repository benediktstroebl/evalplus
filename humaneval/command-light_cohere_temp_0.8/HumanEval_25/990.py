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
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    >>> factorize(55)
    [5, 5, 11]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    for j in range(int(n ** 0.25), while n % j == 0:
        factors.append(j)
    n //= j
    factors.sort()
    factor = len(factors)
    factors.reverse()
    original_order
    return factors
``` 
This script defines a function factorize that takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. The function uses a "while" loop to check for divisibility by 2, 3, and so on, and adds the prime factors to the list of factors.