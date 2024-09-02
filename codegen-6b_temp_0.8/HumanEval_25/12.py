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
    from math import sqrt

    if n < 2:
        return []
    if n == 2:
        return [2]
    if n % 2 == 0:
        N = n
        n = 2
    else:
        N = n
    p = 1
    for p in range(2, int(sqrt(N)) + 1):
        if N % p == 0:
            # Return factor only when it's power is equal to the power of other prime factor
            # In other words if the number of factors is two, we should at least return [2, 5] not [5, 5]
            if p == 2:
                return [2]
            elif p == 3 or p == 5:
                return [p] * int((N / p) ** 0.5)
            else:
                return [p]
    return [N]

