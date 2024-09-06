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
    import math
    n = abs(int(n))
    assert n > 0
    f = []
    last = 0
    next_last = 2
    while n > 1:
        if n % math.gcd(last, next_last) == 0:
            last = next_last
            next_last *= 2
            if n % last == 0:
                f.append(last)
                n //= last
                continue
        last = next_last
        next_last = n // last
    return f


n = int(input())

factors = factorize(n)
cnt = [0] * len(factors)

for factor in factors:
    cnt[factor - 2] += 1
