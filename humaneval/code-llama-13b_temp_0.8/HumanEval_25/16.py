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

    if n < 2:
        return []
    res = []
    while n % 2 == 0:
        res.append(2)
        n /= 2
    k = 3
    while k ** 2 <= n:
        if n % k == 0:
            res.append(k)
            n //= k
        else:
            k += 2
    if n > 2:
        res.append(n)
    return res

