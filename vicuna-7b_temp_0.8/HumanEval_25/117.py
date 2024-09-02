from typing import List


def factorize(n: int) -> List[int]:
    """ Return list of prime factors of given integer in the order from smallest to largest.
    Each of the factors should be listed number of times corresponding to how many times it appeares in factorization.
    Input number should be equal to the product of all factors
    >>> factorize(8)
    [2, 2, 2]
    >>> factorize(25)
    [5, 5]
    >>> factorize(70)
    [2, 5, 7]
    """
    # check if the number is prime
    if n > 1:
        p = 2
        while p * p <= n:
            if n % p == 0:
                return []
            p += 1
        # find the largest prime factor
        p = n
        factors = [p]
        while p > 1:
            p = n // p
            factors.append(p)
        # sort the factors
        factors.sort()
        # return the list of factors
        return factors
    else:
        return []

