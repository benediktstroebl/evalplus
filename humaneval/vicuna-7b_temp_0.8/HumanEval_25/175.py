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
    # base case
    if n == 1:
        return [1]

    # find all prime factors less than sqrt(n)
    prime_factors = [p for p in prime_factors(n) if p < sqrt(n)]

    # keep track of how many times each factor appears
    factor_count = {}
    for p in prime_factors:
        if p in factor_count:
            factor_count[p] += 1
        else:
            factor_count[p] = 1

    # construct list of prime factors
    prime_factors_list = [p for p in prime_factors if p not in factor_count or factor_count[p] == 1]
    return prime_factors_list

