```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    Input number should be a power of two to avoid complex prime factor calculations
    """
    if n <= 1:
        return [n]
    if n <= 3:
        return [1, n]
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    factors.append(int)
    if n % 3 == 0:
        factors.append(3)
        n //= 3
    for i in range(5, int(n ** 0.5) // n // i:
        factors.append(i)
    n //= i
    return factors
```