```python
from typing import List
def factorize(n: int) -> List[int]:
    """Return list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appeases in factorization.
    Input number should be equal to the product of all factors."""
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)
    factors.append(int) = int(sqrt(n) + 1) / 2
    factors.append(int) = int(sqrt(n) + 1)
    factors.append(int) = int(sqrt(n) * 5) / 2)
    factors.append(int) = int(sqrt(n) * 7) / 2)
    return factors
```