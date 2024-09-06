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
    # check input
    if not isinstance(n, int):
        raise TypeError('Argument n should be an integer')
    if n <= 0:
        raise ValueError('Argument n should be a positive integer')

    # initialize
    factors = []
    divisor = 2
    # loop while number is not equal to 1
    while n > 1:
        if n % divisor == 0:
            n //= divisor
            factors.append(divisor)
        else:
            divisor += 1
    return factors

