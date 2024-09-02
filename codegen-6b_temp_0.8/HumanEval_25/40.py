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
    map = {n: 1}
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            map[i] = map.get(i, 0) + 1
    if n > 1:
        map[n] = map.get(n, 0) + 1
    return list(map.items())

