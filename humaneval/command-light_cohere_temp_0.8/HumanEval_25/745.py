```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all factors.
    """
   
    function is essentially implemented to solve the problem.
    """
    prime factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            for j in range(i, n + 1, i):
                prime_factors.append(j)
    if prime_factors == []:
            return []
    else:
        return prime_factors
```