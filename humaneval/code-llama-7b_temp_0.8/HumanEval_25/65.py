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
    def find_next_factor(n, i):
        while i <= n / 2 and n % i != 0:
            i += 1
        return i
    if n < 1:
        raise ValueError("Only positive number can be factorized")
    factors = []
    i = 2
    while n != 1:
        i = find_next_factor(n, i)
        n //= i
        factors.append(i)
    return factors

