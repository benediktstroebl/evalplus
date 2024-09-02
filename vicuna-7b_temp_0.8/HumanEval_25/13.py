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
    if n == 2:
        return [2]
    n = n - 1
    factors = []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            continue
        factors.append(n)
        n = n - 1
    factors = [2] + factors
    while n > 1:
        n = n - 1
        last_factor = factors[-1]
        for i in range(1, len(factors)):
            if factors[i] % last_factor == 0:
                factors[i] = last_factor
        del factors[-1]
    return factors

