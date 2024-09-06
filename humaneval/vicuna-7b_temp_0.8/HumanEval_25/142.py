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
    # if n < 1, throw ValueError
    if n < 1:
        raise ValueError("n should be greater than 1")

    # base case: if n = 1, return [1]
    if n == 1:
        return [1]

    # if n is prime, return it
    if n % 2 == 0:
        return [n]

    # check if n has any prime factors less than or equal to sqrt(n)
    p = 2
    while p <= n // p:
        if n % p == 0:
            break
        p += 1

    # if n has no prime factors less than or equal to sqrt(n), n is its only prime factor
    return [n]
