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
    if n < 2:
        return factors

    while n % 2 == 0:
        factors.append(2)
        n //= 2

    d = 3
    while d * d <= n:
        if n % d == 0:
            factors.append(d)
            n //= d
            counter = 0
            while n % d == 0:
                n //= d
                counter += 1
            factors.extend([d, counter])
        else:
            d += 2

    if n > 1:
        factors.append(n)

    return factors

