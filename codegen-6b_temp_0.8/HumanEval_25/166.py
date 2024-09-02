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
    l = []
    if isinstance(n, int) and n > 1:
        while n % 2 == 0:
            l.append(2)
            n /= 2

        for i in range(3, int(n ** (1 / 2)) + 1, 2):
            while n % i == 0:
                l.append(i)
                n /= i

        if n > 2:
            l.append(n)
        return list(set(l))  # remove duplicate factors
    return l

