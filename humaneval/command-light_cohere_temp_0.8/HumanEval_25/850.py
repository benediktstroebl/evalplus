```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    for i in range(2,int(n**.5)+1):
        if n%i==0:
            factors.append(i)
            n=n//divisors
        elif i>1:
            factors.append(i*factors[0])
    factors.append(n)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of prime factors of n in descending order. Each factor is listed number of times which corresponds to how many times it appears in factorization.