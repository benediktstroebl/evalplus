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
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    >>> factorize(72)
    [2, 2, 2, 3, 3, 3, 6]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i
    for j in factors:
        if j == factors[-1]:
            factors.append( factors.pop(j, 0)
        else:
            factors.append(j)
    return factors
``` 
This function factors an integer n by calculating all its prime factors. It does this using trial and error, meaning it tests various numbers for divisibility until it finds a factor. The process is very efficient, and it doesn't need to go beyond n.