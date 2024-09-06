```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(200)
    [2, 2, 2, 5, 5, 7]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    while n % 3 == 0:
        factors.append(3)
        n = n // 3
    for i in range(5, int(n ** 0.5) // steps, factor=[6, 12...[i]]):
        factors.append(i)
        n = n // i
    for i in range(int(n ** 0.5) + 1, factor=[int(n // i) + 1, i+1]]:
        factors.append(i)
    n = n // i
    return factors
``` 
The function works by checking divisibility by 2 and 3, then uses the sieve of Eratosthenes to find prime numbers up to the square root of n.

The code is self-contained, which means it doesn't rely on any other functions or modules to work.