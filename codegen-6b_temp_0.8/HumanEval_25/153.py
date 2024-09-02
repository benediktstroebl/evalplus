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
    i = 2
    factors = []

    if n == 1:
        return factors
    while n % i != 0:
        i += 1
    factors.append(i)

    if n % i == 0:
        new_phi = n // i
        for j in range(1, new_phi // 2 + 1):
            while n % i == 0:
                n = n // i
            if n % i == 1:
                factors.append(i)
            else:
                i += 2
                while n % i == 0:
                    n = n // i
                if n % i == 1:
                    factors.append(i)
    return factors

