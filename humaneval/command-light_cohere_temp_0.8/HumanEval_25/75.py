```python
from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors is listed number of times corresponding to how many times it appears in factorization of the given number
    Input number should be a product of all its factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # create list of all numbers from 2 to sqrt(n)
    all_factors = [2] + [num for num in range(3, int(sqrt(n))+1, 2)]
    factors = []
    for num in all_factors:
        # find first number that is a factor of n
        while n % num == 0:
            n //= num
        if n == 1:
            factors.append(num)
    else:
            continue
    return factors
```