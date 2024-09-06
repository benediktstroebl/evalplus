```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all its factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # Make sure number is even before starting factorization
    n = n // 2
    factors = []
    while n > 1:
        if n % 2 == 1:
            factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors

# Test the function with a few numbers
print(factorize(8))
print(factorize(25))
print(factorize(70))
```