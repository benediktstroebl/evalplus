```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    :param n: number
    :return: List[int]
    """
    if n < 2:
        return []
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n ** 0.5) + 1,  :  # This is a guess, could be optimized
        for j in range(i, n, i * 2):
            if n % j == 0:
                factors.append(j)
                n = n // j
    if n > 2:
        factors.append(n)
    return factors
```
The function factorizes a given number n into a list of its prime factors in order of increasing magnitude. The function first handles the factors of 2 and then checks for larger prime factors up to the square root of n.