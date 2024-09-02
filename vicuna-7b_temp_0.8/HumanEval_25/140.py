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
    if n < 0:
        return []
    elif n == 0:
        return []
    elif n == 1:
        return [n]
    elif n % 2 == 0:
        return []
    else:
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                return []
        factors = []
        while n > 1:
            p = 2
            while n % p == 0:
                p = p * p
                n = n // p
            factors.append(p)
            n = n // p
        reversed_factors = list(reversed(factors))
        while len(reversed_factors) > 1:
            reversed_factors.pop()
        return reversed_factors

