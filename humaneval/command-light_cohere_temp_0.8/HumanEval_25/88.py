```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times which corresponds to how many times it appears in factorization
    Input number should be equal to the product of all its factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    #make sure number is even
    n = n // 2
    #find the maximum factor in factorization
    m = 2
    while n % m == 0:
        m += 1
        n = n // m
    #make sure m is the largest factor
    p = 2
    while n % p == 0:
        n = n // p
        p += 1
    return [p, n]
```  The function will first ensure that the given number is even, then find the largest factor, and then list both the factor and the number itself, with each occurrence of the factor being twice as often as the number is divisible by the factor.