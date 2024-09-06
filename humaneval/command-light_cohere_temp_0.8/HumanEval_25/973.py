```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times which corresponds to how many times it appears in factorization of the given number
    Input number should be equal to the product of all its factors.

    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(225)
    [3, 3, 5]
    >>> factorize(555)
    [5, 7, 11]
    """
    factors = []
    while n % 2 == 0:
        n /= 2
        factors.append(2)

    for i in range(3, int(n**0.5) + 1, while n % i == 0:
        factors.append(i)
        n /= i

    for i in range(int(n**0.5) + 1, while n % i == 0:
        factors.append(i)

    return factors
```
The above code is a Python script that contains a self-contained function named `factorize`, which calculates and returns the list of prime factors of a given number. It uses a optimized approach to find prime factors by iterating through all possible divisors from 2 up to the square root of the input number, while keeping track of which factors have already been computed.