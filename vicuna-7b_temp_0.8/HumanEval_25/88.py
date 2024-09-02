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
    # The first prime is 2, since 2x2 + 1 is the first form of n = 2^0 \* 3^1
    # We start by listing 2 as the first factor
    factors = [2]
    while n > 1:
        for i in range(1, n):
            if (n % i == 0):
                break
        n //= i
        factors.append(i)
    return factors
