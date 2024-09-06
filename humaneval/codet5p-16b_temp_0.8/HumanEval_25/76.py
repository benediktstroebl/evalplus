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
    res = [2]
    while n > 1:
        for i in range(3, n + 1, 2):
            if i * i > n:
                return res + [n]
            if n % i == 0:
                res.append(i)
                n //= i
                break
    return res
