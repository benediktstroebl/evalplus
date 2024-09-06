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
    factorization = []
    prime_candidate = 2
    while prime_candidate ** 2 <= n:
        while n % prime_candidate == 0:
            n = n / prime_candidate
            factorization.append(prime_candidate)
        prime_candidate += 1
    if n > 1:
        factorization.append(int(n))
    return factorization
