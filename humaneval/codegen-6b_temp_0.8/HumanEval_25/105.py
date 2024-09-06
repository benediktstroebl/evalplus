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
    primes = _get_primes(n)
    factor_list = []
    for i in primes:
        if n % i == 0:
            time = 0
            while n % i == 0:
                time += 1
                n = n // i
            factor_list.append([i, time])
    return [item[0] for item in sorted(factor_list, key=lambda x: x[1])]

