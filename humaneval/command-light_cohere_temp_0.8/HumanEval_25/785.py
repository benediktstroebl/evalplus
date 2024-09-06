```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed in number of times, which corresponds to how many times it appears in the factorization.
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(53)
    [3, 3, 7]
    >>> factorize(78)
    [2, 2, 2, 3]
    >>> factorize(901)
    [3, 3, 4, 4, 6]
    """
    factors = []
    while n % 2 == 0:
        n = n // 2
        factors.append(2)
   
    for i in range(3, int(n**0.5)+1,  #divisible by 2:
        while n % i == 0:
            n = n // i
            factors.append(i)
   
    for i in range(3, int(n**0.5)+1,  # not divisible by 2:
        while n % i == 0:
            factors.append(i **
            n = n // i

```
The provided Python script defines a function called **factorize** that aims to return a list of prime factors for a given integer. The prime factors are identified and listed in the factorization result, with each factor appearing the specified number of times in the factorization. The script utilizes a approach to factorize an integer by considering its divisibility by the smallest even numbers, starting from 2 and progressing up to larger numbers. The function also takes an parameter **n** representing the integer for which the prime factors should be found, and it returns a list of integers that are the prime factors of the given number **n**.