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

    if n < 2:
        raise ValueError("Input number should be greater than 1")
    factors = [1]  # To check if number is prime
    factor = 2
    while factor ** 2 <= n:
        if n % factor:
            factor += 1
        else:
            n //= factor
            factors.append(factor)
    if n > 1:
        factors.append(n)
    return factors

