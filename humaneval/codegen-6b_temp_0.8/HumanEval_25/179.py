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
    if n <= 2:
        return [n]
    l = []
    i = 2
    if n % i == 0:
        while n % i == 0:
            l.append(i)
            n //= i
        if n > 1:
            l.append(n)
    i += 1
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                l.append(i)
                n //= i
            if n > 1:
                l.append(n)
        i += 1
    if n > 1:
        l.append(n)
    return l

