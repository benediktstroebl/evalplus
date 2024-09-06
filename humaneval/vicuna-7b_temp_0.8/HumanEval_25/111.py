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
    # check if number is prime
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return []
        return [n]
    # check if n is 1 or 0
    if n == 1 or n == 0:
        return []
    # recursively find prime factors
    factors = [n]
    while len(factors) > 1:
        # find factors
        for i in range(1, int(n**0.5) + 1):
            for j in range(i**2, n+1, i):
                factors = factors + [j]
        # remove duplicates
        factors = set(factors)
        for factor in factors:
            if factor != n:
                for k in factors:
                    if k != n and k % factor == 0:
                        factors.remove(k)
    return factors

