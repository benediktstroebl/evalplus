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
    while n > 1:
        n = n - 1
        factors.append(n)

    prime_factors = [f for f in factors if f > 1]
    prime_factors_count = Counter(prime_factors)
    result = [p for p in prime_factors if p not in prime_factors_count]
    result.sort(key=lambda x: x // prime_factors_count[x])
    return result

