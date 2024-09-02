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
    factor_numbers = []
    divisor = 2
    while divisor <= n:
        while n % divisor == 0:
            factor_numbers.append(divisor)
            n //= divisor
        divisor += 1

    if n > 1:
        factor_numbers.append(n)

    return factor_numbers

