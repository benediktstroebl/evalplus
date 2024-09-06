```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all factors.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(120)
    [2, 2, 2, 3, 5]
    >>> factorize(500)
    [5, 25, 125]
    >>> factorize(56)
    [2, 2, 2, 7]
    """
    if n <= 1:
        return []
    if n <= 3:
        return [n]
    factors = [i for i in range(2, int(n**0.5) + 1]
    if all(n % i == 0 for i in factors):
        return factors
    else:
        return []
```  This code defines a function called `factorize` that takes an integer `n` as input and returns a list of prime factors of the number, ordered from smallest to largest. The function uses a specific case and an efficient approach to factorize large numbers using trial and error.