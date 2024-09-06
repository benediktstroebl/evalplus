```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factors = factorize(8)
    [2, 2, 2]
    >>> factors = factorize(25)
    [5, 5]
    >>> factors = factorize(70)
    [2, 5, 7]
    """
    if n < 2:
        return []
    factors = []
    for i in range(2, int(n ** 0.5) + 1):
        while not n % i:
            factors.append(i)
            if n != i * i:
                break
    return factors
# Example usage:
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```