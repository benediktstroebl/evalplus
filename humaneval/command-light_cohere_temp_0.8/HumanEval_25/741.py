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
    >>> factorize(120)
    [2, 2, 2, 3, 5]
    >>> factorize(200)
    [2, 2, 5, 2, 2, 2]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5),n //):
        while n % i == 0:
            factors.append(i)
            n = n // i
    for j in range(int(n**0.25),n):
        while n % j == 0:
            factors.append(j)
    return factors
```
This function, factorize, takes an integer n as input and returns a list of prime factors of n in order from smallest to largest. The function first determines if n is less than or equal to 1 and returns an empty list. It then starts a factorizing by dividing n by 2, and then iterates through the integers 3, 5, 7, 9, 11, 13, and so on, dividing n by each prime number until a prime factor is found. The function then returns a list of prime factors of n.