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
    # first check if n is prime
    if n == 1:
        return [n]
    if n % 2 == 0:
        return []
    factors = [n]
    while n > 1:
        # find the largest prime factor
        i = 0
        while n % i == 0:
            i += 1
        if i == 0:
            while n % (i + 1) == 0:
                i += 1
            return factors[:i]
        j = 1
        while n % j == 0:
            j += 1
        if j == 1:
            factors.append(j)
        else:
            factors.append(j)
            # add j^2 to list of factors if it is prime
            if j != n // j:
                factors.append(j * j)
    return factors

