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
    divider = 2
    while n > 1:
        while n % divider == 0:
            prime_factors.append(divider)
            n = n // divider
        divider += 1
        if divider * divider > n:
            prime_factors.append(n)
            break
    return prime_factors

