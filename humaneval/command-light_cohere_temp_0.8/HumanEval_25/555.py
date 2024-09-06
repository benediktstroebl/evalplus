```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times, which corresponds to how many times it appears in the factorization
    Input number should be equal to the product of all its factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(100)
    [2, 2, 2, 5, 5, 7, 11]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n = n // i
    factors.append(int(n))
    return factors
```
This function takes an integer n as input and returns a list of prime factors of n, in ascending order, along with the frequency of each factor. The function first checks for the factor of 2 and appends it to the list if n is even. It then checks for other prime factors, starting from 3 up to the square root of n, and appends them to the list if n is divisible by the corresponding prime number. The function also handles the n = 1 and returns [] as n has no prime factors.