```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times, which corresponds to how many times it appears in the factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    def factor_helper(x):
        factors = []
        divisor = 2
        while x > 1:
            while x % divisor == 0:
                factors.append(divisor)
                x //= divisor
            divisor += 1
        return factors
    return factor_helper(n)
```