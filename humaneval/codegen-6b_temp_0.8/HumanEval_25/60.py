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
    if n < 2:
        return []

    factor = 2
    factors = []

    # if it is divisible by 2, then it is a prime number and we need to add it to the list
    while n > 1:
        if n % factor == 0:
            factors.append(factor)
            n //= factor
        else:
            factor += 1

    # in case of other numbers that are prime, we need to make sure they are in the list only one time
    if n > 1:
        factors.append(n)

    return factors

