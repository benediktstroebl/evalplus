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
    prime_factors = []
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            continue
        if n % 3 == 0:
            n = 3 * n // 6
            continue
        for p in range(5, int(n**0.5) + 1, 2):
            while n % p == 0:
                n = n // p
                break
        if n > 1:
            prime_factors.append(p)
            n = n // p
    return prime_factors