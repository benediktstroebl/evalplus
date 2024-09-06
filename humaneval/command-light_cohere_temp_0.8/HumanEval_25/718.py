```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed in the order of their corresponding multiplicity in the factorization of n.
    """
    numbers are 0, 1, 2, 3, 5, ...
    i = 0
    while n % 2 == 0:
        i += 1
        n /= 2
    j = 0
    while i < j and n > 1:
        j += 1
        if n % j == 0:
            k = n // j
            n -= k
            if k > 1:
                factors.push(k)
    factors.push(j)
factors
    if n > 1:
        factors.push(n)
    return factors
    else:
        return []
    """

# Test the function with different numbers
print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]
```