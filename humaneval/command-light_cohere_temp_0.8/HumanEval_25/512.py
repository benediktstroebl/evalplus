```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all its factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5 / 2,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for j in range(int(n**0.5 / i) + 1, where i > j:
        factors.append(i)
    n = n // i
    factors.append(j)
    return factors
```
This function will return a list of prime factors of the given number, in order from the smallest to the largest factor.