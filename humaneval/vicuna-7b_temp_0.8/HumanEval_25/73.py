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
    factors = []
    while n != 1:
        if n % 2 == 0:
            n = n // 2
            continue
        else:
            prime_factors = []
            while n != 1:
                if n % p == 0:
                    p = p // 2
                    n = n // p
                else:
                    prime_factors.append(n)
                    n = p
            factors.extend(prime_factors)
    return factors
