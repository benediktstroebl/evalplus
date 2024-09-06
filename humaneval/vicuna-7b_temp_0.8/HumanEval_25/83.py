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
    # build list of possible factors
    possible_factors = [2]
    while n > 1:
        # find smallest factor
        smallest = n
        for factor in possible_factors:
            if factor % n == 0:
                if factor < smallest:
                    smallest = factor
        possible_factors.append(smallest)
        n //= smallest

    # build list of factors
    factors = [n]
    while n > 1:
        # find all factors
        for factor in possible_factors:
            if factor % n == 0:
                # add factor to list of factors if it has not been added before
                if factor not in factors:
                    factors.append(factor)
        n //= possible_factors[-1]

    # sort factors by size
    factors.sort(reverse=True)
    return factors

