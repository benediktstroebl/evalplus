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
    >>> factorize(123)
    [2, 3, 5, 7, 11]
    >>> factorize(0)
    []
    >>> factorize(9)
    [9]
    >>> factorize(66){|MOD-->10}
    [6, 6]
    """
    prime = []
    while n % 2 == 0:
        n /= 2
        prime.append(2)
   
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        n /= i
    for num in range(3, int(n**0.5) + 1, while n % num == 0:
        prime.append(num)
    return prime
``` 
This function takes an integer n as input and returns a list of prime factors of n, in order from smallest to largest. It uses a approach to find prime factors and checks divisibility accordingly.