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
    res = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    if n == 1:
        return []
    else:
        while n != 1:
            if n % 2 == 0:
                res.append(2)
                n = n // 2
            elif n % 3 == 0:
                res.append(3)
                n = n // 3
            elif n % 5 == 0:
                res.append(5)
                n = n // 5
            elif n % 7 == 0:
                res.append(7)
                n = n // 7
            elif n % 11 == 0:
                res.append(11)
                n = n // 11
            elif n % 13 == 0:
                res.append(13)
                n = n // 13
            elif n % 17 == 0:
