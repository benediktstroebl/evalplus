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
    p = [2]
    while n!= 1:
        for i in range(len(p)):
            if n % p[i] == 0:
                n //= p[i]
                p.insert(i, p[i])
                break
        if n == 1:
            p.append(n)
    return
