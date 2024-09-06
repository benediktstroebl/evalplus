```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest. The factors are listed according to the number of times it appears in factorization."""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for j in range(int(n**0.5) + 2, 2 * i):
        if n % j == 0:
            factors.append(j)
    return factors
```
The function returns a list of prime factors of the given integer in the order of their appearance in the factorization. It checks for numbers 2, 3, 4, 5, and so on until the number cannot be further factorized.