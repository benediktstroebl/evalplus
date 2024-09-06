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
    >>> factorize(81)
    [3, 3, 7]
    >>> factorize(100)
    [2, 2, 2, 5, 5, 10]
    >>> factorize(55)
    [5, 11]
    """
    s = set(range(2, int(n**0.5) + 1))
   
    for x in s:
        if n % x == 0:
            for y in range(x, int(n**0.5) + 1):
                s.add(y)
            n //= y
   
    # print(f"List of prime factors of {n}: {list(s)})
    return list(s)
```