```python
from typing import List

def factorize(n: int) -> List[int]:
    """
    Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all its factors.
    """
    for i in range(2,int(n**0.5)):
        if n%i == int(n**0.5):
            break
    particular factor is found, return list of the factor and 
        increment factor counter
        """
    factors = []
    for i in range(2, int(n**0.5)):
        if n % i == int(n**0.5):
            factors.append(i)
            factors.append(i)
            factors.append(i)
            factors.append(i)
   
    return factors
```