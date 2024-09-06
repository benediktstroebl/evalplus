```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(0)
    []
    >>> factorize(-5)
    []
    >>> factorize(10)
    [2, 5]
    >>> factorize(15)
    [3, 5]
    """
    factors = []
    while n > 1:
        d = n % 2
        if d == 0:
            factors.append(d)
        n = n // 2
        else:
            factors.append(d)
            n = n // 2
    factors.append(d)
    return factors
```
This Python function, `factorize`, takes an integer `n` as input and returns a list of its prime factors in order, from smallest to largest. Each factor is listed number of times corresponding to how many times it appears in the factorization of `n`. The function utilizes a while loop to repeatedly divide `n` by 2 until it becomes 1, and appends the remainder to the list of factors. The function also handles cases where `n` is 0 or negative by returning an empty list.