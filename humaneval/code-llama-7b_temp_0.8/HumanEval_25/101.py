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
    from functools import reduce
    from math import sqrt

    # return [p for p in range(1, int(sqrt(n)) + 1) if n % p == 0]
    prime_factors = []
    i = 1
    while n > 1:
        if n % i == 0:
            prime_factors.append(i)
            n /= i
            i = 1
        else:
            i += 1
    return reduce(list.__add__, [[x] * prime_factors.count(x) for x in prime_factors])
