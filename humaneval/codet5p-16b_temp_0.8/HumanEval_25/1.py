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

    prime_factors = []
    p = 2
    while p <= n:
        count = 0
        while n % p == 0:
            count += 1
            n //= p
        if count > 0:
            prime_factors.append(p)
        p += 1
    return prime_factors

