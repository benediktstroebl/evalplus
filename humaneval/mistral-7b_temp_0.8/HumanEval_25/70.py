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

    # determine which number is smallest power of
    i = 2
    while n % i:
        i += 1

    # loop over number of prime factors of n
    while n != 1:
        # insert factors into list in order from smallest to largest
        factors.append(i)

        # get the power of the current factor in factorization of n
        factor_power = 0
        while n % i == 0:
            n //= i
            factor_power += 1

        i += 1
        while n % i:
            i += 1

    return factors
