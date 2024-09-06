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
    # Find all prime factors
    factors = []
    cur = 2
    while cur**2 <= n:
        if n % cur != 0:
            cur += 1
            continue
        n //= cur
        factors.append(cur)
    factors.append(n)
    return factors

