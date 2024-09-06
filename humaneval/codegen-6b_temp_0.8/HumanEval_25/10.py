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
    exponent = 0
    p_factor = 2
    factors = []
    while n > 1:
        while n % p_factor == 0:
            n //= p_factor
            exponent += 1
        if exponent > 0:
            factors.append(p_factor)
            exponent = 0
        p_factor += 1

    return factors

