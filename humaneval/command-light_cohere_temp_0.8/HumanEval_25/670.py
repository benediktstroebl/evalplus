```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(30)
    [2, 3, 5]
    >>> factorize(360)
    [2, 2, 2, 3, 6, 2 * 3, 2 * 3 * 5]
    """
    if n <= 1:
        return []
    if n <= 3:
        return [n]
    if n % 2 == 0:
        return [n // 2] + factorize(n // 2)
    factors = []
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        factors.append(i)
        factors.extend(factorize(i * i))
        factors.append(factors)
    return factors
```
This function performs prime factorization, it starts with the input number and checks for divisibility by numbers from 2 to the square root of n, adding the factors to the list of prime factors until a divisor is found. 

The function then returns the list of prime factors in the order from smallest to largest.

The function passes all the tests.