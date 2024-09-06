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
    def get_factors(n: int) -> List[int]:
        if n < 2:
            return []
        factors = []
        while n > 1:
            if n % 2 == 0:
                n //= 2
                continue
            factors.append(2)
            n //= 2
        factors.extend(get_factors(n // 2))
        return factors

    factors = get_factors(n)
    result = []
    for factor in factors:
        count = 1
        while factor * count != n:
            count *= factor
        result.append(factor * count)
    return result
