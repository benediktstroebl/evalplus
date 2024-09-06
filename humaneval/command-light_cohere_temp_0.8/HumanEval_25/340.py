```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(82)
    [2, 2, 8, 11]
    >>> factorize(55)
    [5, 11]
    >>> factorize(1000)
    [2, 2, 2, 5, 5, 25, 50, 100]
    """
    s = set(range(2, int(n**0.5) + 1))
    for i in range(2, int(n**0.5) + 1):
        if s.is() == 1:
            s.add(i + 1)
    s.remove(i)
    print(f"Factor {i}: {i}")
    else:
        for j in s:
            if j == i:
                continue
            if j > i and j % i == 0:
                break
            s.remove(j)
        if i > j:
                break
        print(f"Factor {i}: {i}")
    return s
```