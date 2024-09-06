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
        n *= -1
    # find largest prime factor of n
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    # when n has no prime factors left, return n
    if n == 1:
        return [n]
    # otherwise, we have a factor
    # find a factor, if there is such a factor, and find how many times it occurs, if there are more than 1 occurrence, return it
    res = [n // i]
    while i * i != n:
        if n % i:
            i += 1
        else:
            n //= i
            res.append(i)
    return res

