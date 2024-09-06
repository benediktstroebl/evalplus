```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []

    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)

    for i in range(3, int(n ** 0.5) + 1,):
        while n % i == 0:
            n /= i

    for i in range(5, int(n ** 0.5) + 1):
        while n % i == 0:
            factors.append(i)

    return factors
```
This script defines a function called `factorize` that returns a list of prime factors of a given integer `n`. It first checks if `n` is less than or equal to 1 and returns an empty list. If `n` is greater than 1, it proceeds to find the prime factors by dividing by 2 repeatedly until the number becomes odd, and then checks for divisibility by the odd prime numbers from 3 to the square root of `n` up.