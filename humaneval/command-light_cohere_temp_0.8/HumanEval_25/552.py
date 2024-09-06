```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    1s, 2s, and 3s are always factors. But 4s and greater numbers are not always prime. """

   
    from smallest possible number using divisibility test until it fails and its next number comes into play.
    """ The numbers greater than 4 are always divisible by 2 and can be factorized by 2 and 3.
    """
    n must be a positive integer greater than 2"""
    factors = []
    while n != 1:
        if n % 2 == 0:
            factors.append(2)
            n = n // 2
        elif n % 3 == 0:
            factors.append(3)
            n = n // 3
        else:
            m = n // high(n, 5)
            factors.append(high(n, 5))
            n = n // m
    return factors
def high(n: int, m: int) -> int:
    """ Compute the mth power function, i.a.e, n=s large factor on a number and return the result of the m power function of n to the power of m.
    """ For numbers 4, 6, 8, 10, etc. You can always use the positive exponentiation function to get the result.
```