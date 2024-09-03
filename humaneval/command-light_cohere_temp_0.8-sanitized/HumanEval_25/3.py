from typing import List
def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    >>> factorize(55)
    [5, 11]
    >>> factorize(666)
    [2, 2, 3, 3, 6, 6]
    """
    factors = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if len(factors) == i:
                factors.remove(factors[0])
                break
    return factors