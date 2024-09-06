```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    Input:
    n: int (the number to find prime factors for)
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5),  #n % 2):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for j in range(int(n**0.5) - 2):
        if n % j == 0:
            factors.append(j)
            n = n // j
    return factors
```