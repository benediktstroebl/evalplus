```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    This factors should be listed number of times corresponding to how many times they appear in factorization.
    """
    factorize(8)
    [2, 2, 2]
    """
    return list(set(x for x in range(1, n+1) if n % x == 0))
```