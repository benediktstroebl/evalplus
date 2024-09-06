```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest. Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    for i in range(3, int(n**0.5), i + 1):
        factors.append(i)
        n = n // i
    while len(factors) > 1:
        if factors[-1] > factors[-2]:
            factors.append(factors.pop()
        list by removing last element
        else:
            factors.append(factors[-2])
            factors.pop()
    if factors.pop()
        listby list of factors to keep the order. 
```
This function uses the approach of identifying the factors and their corresponding times in the factorization of the number.