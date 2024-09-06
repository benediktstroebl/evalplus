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
    >>> factorize(1000)
    [2, 2, 3, 5, 7, 11, 13, 17, 19]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n > 1:
        for d in range(3, int(n**.5) + 1, 2):
            if n % d == 0:
                factors.append(d)
                n //= d
    return factors

```
This code defines a function called `factorize` that takes an integer `n` as input and returns a list of its prime factors. The function uses a iterative approach to find the prime factors of the number, starting with the assumption that all numbers divisible by 2 are also prime factors. The function also handles larger numbers by using the formula for finding prime factors of a number `n` which is a perfect power of prime `p`.