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
    if n <= 1:
        return []
    i = 2
    while i * i <= n:
        if n % i == 0:
            cnt = 0
            while n % i == 0:
                cnt += 1
                n //= i
            factors.append([i, cnt])
        i += 1
    if n > 1:
        factors.append([n, 1])
    return factors

