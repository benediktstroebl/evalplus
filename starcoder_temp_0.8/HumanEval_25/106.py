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

    # collect all prime factors of the number and number of their occurances
    factors = {}
    while n % 2 == 0:
        factors.setdefault(2, 0)
        factors[2] += 1
        n /= 2
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.setdefault(i, 0)
            factors[i] += 1
            n /= i
    if n > 2:
        factors.setdefault(n, 0)
        factors[n] += 1

    return list(factors.items())
