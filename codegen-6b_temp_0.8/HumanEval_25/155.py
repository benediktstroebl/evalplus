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
    if n < 0:
        raise ValueError("Factorize is only defined for non-negative integers")

    if n == 0:
        return []

    lst = []
    while n % 2 == 0:
        lst.append(2)
        n /= 2
    i = 3
    while i <= n**0.5:
        if n % i == 0:
            lst.append(i)
            n /= i
            i = 3
        else:
            i += 2

    if n > 2:
        lst.append(n)

    return lst

