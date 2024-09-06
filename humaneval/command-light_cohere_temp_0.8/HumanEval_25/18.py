```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(200)
    [2, 2, 2, 5, 5, 7]
    >>> factorize(300)
    [2, 3, 5, 7]
    >>> factorize(1000)
    [2, 2, 2, 3, 3, 5, 7, 3]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    factors.append(int(1))
    for i in range(3, int(n**0.5)+1, i+=1:
        factors.append(int(i))
    return factors
```
Do you need anything else?