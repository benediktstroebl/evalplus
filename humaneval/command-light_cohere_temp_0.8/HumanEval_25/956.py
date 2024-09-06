```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are returned as numbers corresponding to the times they appear in factorization
    Input number should be equal to the product of all its factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(110)
    [2, 5, 5, 5, 11]
    >>> factorize(216)
    [2, 2, 2, 3, 3, 6]
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
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            factors.append(num)
    n = n // num
    return factors
```
This function utilizes the process of factorization to identify the prime factors of a given integer n. The process starts by checking if n is less than or equal to 1, and returns an empty list if true. The function then iterates through the process of dividing n by increasing numbers until the divisor results in a remainder of 0. It is evident that these divisors are prime factors of n, and are added to the list of factors. The function also handles the cases of even and odd numbers, where the prime factors are the divisors that result in a remainder when divided by n.