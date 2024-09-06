```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    A factor is a any number that can be divided evenly by the given number.
    Also, the factors will be listed in the order of their appearance in factorization.
    Input number should be equal to the product of all factors
    """
    factors = []
    for i in range(1,int(n**.5)+1): 
        is_divisible = n%i == 0 
        if is_divisible:
            factors.append(i)
            factors.append(factors.pop() if isis the same factor, as the number is divisible by all factors.
    factors.sort()
    last list of prime factors of n
    """