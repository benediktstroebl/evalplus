```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(3629)
    []
    """
    factors = []
    while n > 1:
        if n % 2 == 0:
            factors.append(2)
        n = n // 2
    while n > 1:
        if n % 3 == 0:
            factors.append(3)
        n = n // 3
    while n > 1:
        if n % 5 == 0:
            factors.append(5)
        n = n // 5
    while n > 1:
        if n % 7 == 0:
            factors.append(7)
        n = n // 7
    factors.append(int(n))
    return factors
``` 
This script defines a function called `factorize` that takes an integer n as input and returns a list of prime factors of n in the order of their greatest exponent. The function uses a strategy of iterating through the numbers 2, 3, 5, 7, calculating the remainder when divided by each of these numbers until the remainder becomes 0, at which point the number is either a prime or not.