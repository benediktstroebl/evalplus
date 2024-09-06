```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    if n <= 1:
        return []
    if n <= 3:
        return [n]

    prime = []
    for i in range(2, int(n ** 0.5) + 1):
        while True and n % i == 0:
            prime.append(i)
            n = n // i

    return prime

```  This function, `factorize()`, takes an integer `n` as input and returns a list of its prime factors in order, from smallest to largest. The function uses the technique of testing each potential factor and checking if it divides the number evenly.