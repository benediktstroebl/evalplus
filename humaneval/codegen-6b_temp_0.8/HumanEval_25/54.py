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
    """

    1. define a condition, so that the list is updated when it's updated

    2. start from i=2, i is the prime number, divide it by 2,
    how many times is the number divisible by 2
    if the number is divisible by 2, divide it by 2,
    how many times is the number divisible by 2

    """

    res = []
    visited = [False] * (n+1)
    i = 2
    while i * i <= n:
        while n % i == 0:
            res.append(i)
            n //= i
            visited[i] = True
        i += 1
        while not visited[i]:
            i += 1

    if n > 1:
        res.append(n)

    return res


import unittest

