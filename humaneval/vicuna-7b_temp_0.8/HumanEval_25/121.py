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
    p = 2
    while p <= n:
        if n % p:
            # factor found
            if not any(n % d for d in factors):
                return [p] + [(n // d) for d in factors]
            else:
                # adjust factors
                while n % p:
                    p += 1
                return [p] + [(n // d) for d in factors]
        p += 1
    # should never reach this point
    return []

