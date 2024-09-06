```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest
    Each of the factors should be listed number of times, which corresponds to how many times it appears in the factorization
    >>> factorize(8)  # [2, 2, 2]
    >>> factorize(25) # [5, 5]
    >>> factorize(70) # [2, 5, 7]
    >>> factorize(500) # [2, 2, 5, 5, 7, 11, 13]
    >>> factorize(500000) # [2, 2, 5, 5, 7, 11, 13, 169]
    """
    if n <= 1:
        return []

    if n % 2 == 0:
        temp = n // 2
        return [temp] + factorize(temp)

    factors = []
    for i in range(3, int(n ** 0.5) + 1, while n % i == 0:
        temp = i
        while n % temp == 0:
            n //= temp
            temp += 1
        factors.append(temp)

    return factors
``` 
This Python function called `factorize` takes an integer `n` as input and returns a list of prime factors of the given number. It uses a analytical and iterative approach to find the prime factors of the number and the order of the factors is maintained.