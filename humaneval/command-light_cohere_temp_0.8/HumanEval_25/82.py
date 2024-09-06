```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization of the number.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 5, 5, 7, 11]
    >>> factorize(5429)
    [7, 3, 3, 7, 7, 11]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        n = n / 2
        factors.append(2)
   
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n / i
    factors.append(i)
    return factors
```
This Python function, `factorize`, is designed to return a list of prime factors for a given integer `n`. It uses a loop to repeatedly divide by 2 until the number becomes odd, and then checks for divisibility with numbers 3, 7, 13, etc. Each of these numbers is added to the `factors` list as long as they divide `n` evenly.