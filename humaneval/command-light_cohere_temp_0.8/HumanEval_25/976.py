```python
from typing import List
def factorize(n):
    """ Return list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors."""
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(n**0.5) + 1,):
        while n % i == 0:
            factors.append(i)
            n = n // i

    factors.append(n)
    return factors
```
This function employs the `Factorization` algorithm to determine the list of prime factors of a given integer. The algorithm consists of two primary operations: dividing the number by 2 until the number is no more divisible by 2, and then using the remaining prime factors to divide the number further, following their order of appearance in the factorization.