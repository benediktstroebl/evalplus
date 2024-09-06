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
    if n % 2 == 0:
        counter = 0
        while n % 2 == 0:
            counter += 1
            n = n // 2
        factors.append(counter)
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            counter = 0
            while n % i == 0:
                counter += 1
                n = n // i
            factors.append(counter)
    if n > 2:
        factors.append(1)
    return factors

