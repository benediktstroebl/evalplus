```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Returns list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5), step by step):
        if n % i == 0:
            factors.append(i)
            n = n // i
    for j in range(int(n**0.5) - 1, j -= 1:
        factors.append(j)
    return factors
```