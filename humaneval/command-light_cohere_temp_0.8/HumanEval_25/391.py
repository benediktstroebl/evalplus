```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    Input number should be a power of 2 (for efficiency)
    """
    if n <= 1:
        return []

    if n == 2:
        return [2]

    # initialize factors list
    factors = [0]

    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        factors.append(i)
        n //= i

    for i in range(int(n ** 0.5) + 1, while n % i == 0 and i <= factors[-1] + 1:
        factors.append(i)

    # return list of prime factors in order from smallest to largest
    return factors
```