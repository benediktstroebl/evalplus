```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be the same number of times in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(91)
    []
    >>> factorize(55)
    [3, 3, 5]
    """
    if n <= 1:
        return []
    i = 2
    while i * i <= n:
        if n % i == 0:
            temp = [i]
            while n % temp[0] == 0:
                n //= temp[0]
                temp.append(temp.remove(temp.insert(temp.pop())
                factors into the context for all prime factors.
    return temp

    temp.remove(temp)
    if n > 1:
        return [n] + temp
```