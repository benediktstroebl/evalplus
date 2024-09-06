```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization.
    Input number should be equal to the product of all factors
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    for num in factors:
        factors.append(factors.count(num))
   
    return factors
```
This function uses the same algorithm as the previous code, but organized a bit better. The function first finds all factors of 2 and then iterates upwards until the square root of the number is greater than the number.  This approach is more efficient and requires less calculations.