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

    result: List[int] = []

    # Phase 1: Find all prime factors
    prime_factors: List[int] = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    for i in range(3, int(n ** 0.5) + 1, 2):
        while n % i == 0:
            prime_factors.append(i)
            n //= i
    if n > 2:
        prime_factors.append(n)

    # Phase 2: Find number of times each prime factor appears in factorization
    for i in prime_factors:
        result.append(prime_factors.count(i))

    return result

