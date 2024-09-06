```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # Set of prime numbers
    prime = [2, 3, 5, 7, 11, 13, 17, 19]
    factor = []
    for i in range(2, int(n**0.5) + 1):
        while not n % i:
            while n % i == 0:
                n //= i
            factor.append(i)
        if i == int(n**0.5):
            else: pass

    # Sort the list to ensure the order of factors is always the same.
    return factor
sort(factor)
    return factor
```