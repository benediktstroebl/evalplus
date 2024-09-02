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
    def is_prime(n: int) -> bool:
        """ Returns True if n is prime, else False """
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def get_factors(n: int) -> List[int]:
        """ Return list of prime factors of given number in ascending order"""
        if n > 1:
            p = 2
            while n % p == 0:
                p += 1
            return [p]
        else:
            return []

    if not is_prime(n):
        return []
    p = 2
    while n > 1:
        n = n // p
        p += 1
    return get_factors(n)

