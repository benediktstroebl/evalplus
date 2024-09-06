```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    :type n: int
    :return: list of integers
    """
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5), _sqrt(n)):
        factors.append(int(n // i * i))
    for num in factors:
        if num > 1:
            factors.append(num)
    return factors
```
The function returns a list of prime numbers that are factors of the given number.  It sorts the factors in ascending order, with the smallest factor first and the largest factor last.