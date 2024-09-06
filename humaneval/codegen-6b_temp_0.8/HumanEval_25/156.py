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
    factors = []

    # Check for 2
    if n % 2 == 0:
        if n == 2:
            return [2]
        else:
            factors.append(2)

    # Check for other divisors
    for i in range(3, n + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # Check for last remainder factor
    if n > 1:
        factors.append(n)

    return factors

