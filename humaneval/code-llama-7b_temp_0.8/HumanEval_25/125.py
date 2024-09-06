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
    if n <= 0:
        return []

    def prime_factors(n):
        pf = []
        div = 2
        while n != 1:
            if n % div == 0:
                pf.append(div)
                n //= div
            else:
                div += 1
        return pf

    return prime_factors(n)

