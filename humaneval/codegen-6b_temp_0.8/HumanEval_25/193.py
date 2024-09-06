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
    assert n > 0, "Number has to be positive"

    factors = []

    # At a time each number divides n and is a factor of the number
    # factorize(n) is list of factors of n
    # The length of factors is len(factorize(n)) - 1
    #  factors = [a, b, c, d, e, f, g, h, i, j, k, l, m, n]
    #   len(factors) = 13
    #   factors[0] = n
    #   len(factors[0]) = 1
    #   factors[1] = a
    #   len(factors[1]) = 2
    #   factors[2] = b
    #   len(factors[2]) = 2
    #   factors[3] = c
    #   len(factors[3]) = 2
    #   factors[4] = d
    #   len(factors[4]) = 2
    #   factors[5] = e
    #   len(factors[5]) = 2
    #   factors[6] = f
    #   len(factors[6]) = 2
    #   factors[7] = g
    #   len(factors[7]) = 2
    #   factors[8] = h
    #   len(factors[8]) = 2
    #   factors[9] = i
    #   len(factors[9]) = 2
    #   factors[10] = j
    #   len(factors[10]) = 2
    #   factors[11] = k
    #   len(factors[11]) = 2
    #   factors[12] = l
    #   len(factors[12]) = 2

    #   factors[0] = n
    #   len(factors[0]) = 1
    #   factors[1] = a
    #   len(factors[1]) = 2
    #   factors[2] = b
    #   len(factors[2]) = 2
    #   factors[3] = c
    #