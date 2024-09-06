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
    """
    if n <= 1:
        return []
    if n <= 3:
        return [n]
    if n % 2 == 0:
        return [2] + factorize(n // 2)
    factors = []
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        factors.append(factors.pop() if a took from 3 * 6, since we can use prime factorization to list factors)
    return factors

# example usage:
```
n = 70
factors = factorize(n)
print(factors)  # Output: [2, 5, 7]
```