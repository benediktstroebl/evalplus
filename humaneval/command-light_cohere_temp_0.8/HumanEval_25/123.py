```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(50)
    [2, 5, 5]
    >>> factorize(1000)
    [2, 2, 2, 5, 5, 7, 11]
    """
    s = set(range(2, int(n**0.5)+1))
   
    factors = []
    for i in s:
        if n % i == 0:
            factors.append(i)
            if i!=1: factors.append(i * n // int(n**0.5)
   
   
    a set of prime factors of n.

```  This script defines a function called factorize that takes an integer n as input and returns a list of prime factors of n, in order from smallest to largest, using a set of numbers from 2 to the square root of n. You can use this fact as a test to ensure that the function is correct and self-contained.