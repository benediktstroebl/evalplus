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
    factor_set = set()
    factors = [1, 2, 3]
    while n > 1:
        for i in factors:
            if n % i == 0:
                factor_set.add(i)
                n //= i
                break
        else:
            factors.append(n)
            n = 1
    return sorted(factor_set, reverse=True)

