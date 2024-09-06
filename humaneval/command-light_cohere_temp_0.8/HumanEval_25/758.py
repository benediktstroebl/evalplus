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
    # list of all factors that are less than or equal to sqrt(n)
    factors = []
    for i in range(1, int(n**0.5)+1):
        while n % i == 0:
        factors.append(i)
        n //=i
    for i in range(2, int(n**0.5)+1): while n % i == 0:
        factors.append(i)
        n //=i
    for i in range(int(n**0.5)+1, while n % i == 0:
        factors.append(i)
        n //=i
    factors.sort()
    unique_prime = []
    for i in factors:
        if i not in unique_prime:
            unique_prime.append(i)
    return unique_prime
```