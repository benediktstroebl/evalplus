```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are returned number of times which corresponds to how many times it appears in the factorization of the number.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n > 1:
        if n % 3 == 0:
            factors.append(3)
        n = n // 3
        elif n % 5 == 0:
            factors.append(5)
        n = n // 5
        elif n % 7 == 0:
            factors.append(7)
        n = n // 7
    factors.append(n)
    return factors
```
This script defines a function called `factorize` which takes an integer `n` as input and returns a list of its prime factors in the order of their appearance. 

The function uses a while loop to factorize the number and checks for the different prime factors. The loop starts by dividing the number by 2 and checking for divisibility. Then, it checks for the divisibility by 3, 5, and 7.