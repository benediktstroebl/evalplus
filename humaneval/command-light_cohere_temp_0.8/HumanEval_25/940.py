```python
from typing import List

def factorize(n: int) -> List[int]:
    """ Returns list of prime factors of given integer in the order from smallest to largest
    Each of the factors are listed in the order of the corresponding number of times it appears in factorization
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(10)
    [5]
    >>> factorize(27)
    [3, 3]
    >>> factorize(55)
    [5, 11]
    >>> factorize(360)
    [2, 2, 3, 6]
    """
    if n <= 1:
        return []

    # make sure n is an odd number
    n += n%2

    # handle the special case of 2n being even
    if n % 2 == 0:
        return [n//2, 2]

    # 2s and odd divisors less than sqrt(n)
    factors = [2] + [d for d in range(3, int(n**0.5),sqrt(n),divmod(n, 2))]

    # n is even
    # handle case where all the odd divisors are less than sqrt(n)
    if len(factors) > 1:
        for i in range(len(factors) - 1):
            factors[i] += factors[i+1]

    # handle the case where n is a perfect square
    if n % 4 == 1:
        return [2] + [n//2] * [2] * 2

    # n is a perfect square
    else:
        return [2] + [n//2] * [2]

    # return the list of prime factors
    return factors

```