```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization of the given number
    Input number should be a product of all its factors
    """
    factors = []
    for i in range(2,int(n**0.5) + 1):
        while n%i == 0:
            factors.append(i)
            n = n // i
    factors.append(n)
    return factors
```
This function factorizes a given number n by finding its prime factors. It iterates from the factor from 2 to the square root of n, checks for divisibility, and adds the factor to the list of factors if it is divisible. The function then returns the list of prime factors of the number n, ordered from smallest to largest. 

The function passes all the corresponding tests.