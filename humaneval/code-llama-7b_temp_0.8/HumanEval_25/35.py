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
    factors = []
    if n == 1:
        return factors
    while n > 1:
        if n % 2 == 0:
            n /= 2
            factors.append(2)
            continue
        for p in range(3, int(n ** 0.5) + 1, 2):
            if n % p == 0:
                n /= p
                factors.append(p)
                break
        else:
            factors.append(int(n))
            n = 1
    return factors

