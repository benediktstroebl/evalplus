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
    """
    if n <= 1:
        return []
    elif n <= 3:
        return [n]
    else:
        factors = []
        while n % 2 == 0:
            n //= 2
            factors.append(2)
        factors.
        for i in range(3, int(n**.5), by=2):
            while n % i == 0:
                n //= i
                factors.append(i)
        return factors
```  This code defines a function called `factorize` that takes an integer n as input and returns a list of prime factors of n in order of size from smallest to largest, along with the count of each factor in the factorization. The function uses a loop to find all the prime factors of n.