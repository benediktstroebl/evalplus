```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(91)
    [7, 3, 3]
    >>> factorize(77)
    [7, 11]
    >>> factorize(3284)
    [2, 2, 2, 17]
    """
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    return factors

``` 
Do you have any other code related questions you would like assistance with?  I can provide assistance with the development and implementation of various programs.   Feel free to ask if you would like to clarify any potential topics!