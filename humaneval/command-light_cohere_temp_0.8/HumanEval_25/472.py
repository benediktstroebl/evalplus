```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors.
    """ Example list of prime factors, starting from 2, will only contain factors 2 and 3, until the number exceeds 2^6.
    """ Example and all numbers with possible prime factors, up to the square root of the input number."""
    factors = []
    while n >= 2:
        count = 0
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                count += 1
                factors.append(i)
                n = n // i
        if count > 0:
            factors.append(count)
        else:
            factors.add( factors[:] + [count + 1])
    return factors
```