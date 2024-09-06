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
    all_factors = []
    factors = {n: 1}

    if n == 1:
        return all_factors

    p = 2
    if n % p == 0:
        factors[p] = 0
        while n % p == 0:
            factors[p] += 1
            all_factors.append(p)
            n = n / p

    limit = int(n ** 0.5) + 1
    p = 3
    if n % p == 0:
        factors[p] = 0
        while n % p == 0:
            factors[p] += 1
            all_factors.append(p)
            n = n / p

    if n > limit:
        p = 3
        limit = int(n ** (1 / 2)) + 1
        if n % p == 0:
            factors[p] = 0
            while n % p == 0:
                factors[p] += 1
                all_factors.append(p)
                n = n / p

    if n > limit:
        p = 2
        limit = int(n ** (1 / 3)) + 1
        if n % p == 0:
            factors[p] = 0
            while n % p == 0:
                factors[p] += 1
                all_factors.append(p)
                n = n / p

    while n > 1:
        if n % 2 == 0:
            factors[2] = 0
            while n % 2 == 0:
                factors[2] += 1
                all_factors.append(2)
                n = n / 2

        max_p = int(n ** 0.5) + 1
        p = 3
        if n % p == 0:
            factors[p] = 0
            while n % p == 0:
                factors[p] += 1
                all_factors.append(p)
                n = n / p

        if n > limit:
            p = 3
            limit = int(n ** (1 / 3)) + 1
            if n % p == 0:
                factors[p] = 0
                while n % p