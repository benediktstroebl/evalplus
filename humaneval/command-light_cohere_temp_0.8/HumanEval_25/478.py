```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.
    """
    done
    done by:
    all factors are found.
    factor: [2, 4, 3, 1]
    """
    if n < 2:
        return []
    factors = []
    for i in range(2, n + 1):
        if n % i == 0:
            factors.append(i)
            n //= i
    factors.append(n)
    return factors
```