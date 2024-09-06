```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5), i+ i+2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for j in factors:
        if j == factors[-1]:
            factors.append(factors.pop(0)
        else:
            factors.append(j)
    return factors
```

This function takes an integer n as input and returns a list of prime factors of n in order from smallest to largest. The function first checks if n is less than or equal to 1 and returns an empty list if n is not greater than 1. Then, the function enters a while loop and keeps adding the smallest prime factor to n and dividing n by this prime factor until n is no divisible by this prime factor anymore. The function then checks if the list of prime factors is the same as the last one and returns them if it is. If not, it appends the next prime factor to the list of prime factors.