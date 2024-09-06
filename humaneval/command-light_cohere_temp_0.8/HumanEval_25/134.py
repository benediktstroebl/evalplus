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
    >>> factorize(111)
    [3, 3, 3]
    >>> factorize(300)
    [2, 2, 3, 3, 3]
    """
    if n <= 1:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    for j in range(int(n ** 0.5) + 1, while n % j == 0:
        factors.append(j)
    n = n // j
    for k in range(int(n ** 0.5) + 1, while n % k == 0 and k <= j:
        factors.append(k)
        n = n // k
    return factors
``` 
This function takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. It employs a trial and error approach to find the prime factors of a given number and utilizes the listing of factors in the factorization.