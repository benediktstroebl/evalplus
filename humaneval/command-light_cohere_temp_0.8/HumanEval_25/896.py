```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed number of times corresponding to how many times it appears in factorization
    Input number should be equal to the product of all the factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
        while n % 2 == 0:
            factors.append(2)
            n //= 2
    for num in range(3, int(n**0.5) //, n %= num:
        factors.append(num)
        return factors
```

The code first attempts to find the factors using the while loop. It adds the 2 to the list of factors when the number is even. It adds the 2 repeatedly until the number is even. It adds all odd numbers greater than 3 up to the list of factors until the number is not divisible by the number.