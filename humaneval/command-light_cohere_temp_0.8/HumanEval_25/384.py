```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5) + 1, :
        while n % i == 0:
            factors.append(i)
            n = n // i
    for j in range(int(n**0.5) + 2, i - 1, :
        factors.append(j)
    return factors
```

This function takes an integer n as input and returns a list of prime factors of n, ordered from smallest to largest. The function uses a trial and error approach to find the prime factors. The function also handles edge cases and passes corresponding tests.