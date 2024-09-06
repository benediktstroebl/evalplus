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
    # check if n is prime
    if not n % 1:
        return [n]

    # check if n is prime
    if not n % 2:
        return [2, n]

    # check if n is prime
    if not n % 3:
        return [3, n]

    factors = []

    # keep track of prime factors
    p = 2
    while p <= math.sqrt(n):
        if n % p:
            factors.append(p)
        p += 1

    # check if n is prime
    if not n % 4:
        return [4, n]

    # keep track of factors
    p = 4
    while p <= math.sqrt(n):
        if n % p:
            factors.append(p)
        p += 1

    # add the next prime factor
    factors.append(n % 4)

    # check if n is prime
    if not n % 5:
        return [5, n]

    # keep track of factors
    p = 5
    while p <= math.sqrt(n):
        if n % p:
            factors.append(p)
        p += 1

    # add the next prime factor
    factors.append(n % 5)

    # check if n is prime
    if not n % 6:
        return [6, n]

    # keep track of factors
    p = 6
    while p <= math.sqrt(n):
        if n % p:
            factors.append(p)
        p += 1

    # add the next prime factor
    factors.append(n % 6)

    # check if n is prime
    if not n % 7:
        return [7, n]

    # keep track of factors
    p = 7
    while p <= math.sqrt(n):
        if n % p:
            factors.append(p)
        p += 1

    # add the next prime factor
    factors.append(n % 7)

    # check if n is prime
    if not n % 8
