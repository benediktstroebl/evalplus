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
    # Find the number of prime factors
    num_factors = len(list(primes))
    if n % 2 == 0:
        n = n + 1
        num_factors -= 1

    # Find prime factors
    factors = []
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            continue
        for i in range(num_factors):
            if n % primes[i]:
                break
        else:
            factors.append(n)
            n = primes[i]

    return factors