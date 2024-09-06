```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(50)
    [2, 5, 5, 5]
    >>> factorize(100)
    [2, 2, 5, 5, 5]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5)+1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n**0.5)+2, while n % j == 0:
        factors.append(j)
    n = n // j
    factors.append(n)

    return factors
```
This function takes an integer n as input and returns a list of its prime factors in order of appearance, and each factor is listed number of times corresponding to its frequency in factorization of the number n.