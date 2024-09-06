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
    >>> factorize(300)
    [2, 2, 3, 5, 7, 5]
    >>> factorize(13)
    []
    """
    if n <= 1:
        return []
    
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    i = 4
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
        i += 2
    factors.append(int(factorial(i)))
    
    return factors
``` 
The function iterates through the numbers, starting from 2 and adding prime factors as it goes. 

It is a recursive implementation that checks divisibility by progressively larger numbers and adds the factors accordingly. 

The code is written without using any external libraries, using only standard Python types and functions.