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
    prime_factors = []
    current_sum = n
    while current_sum > 1:
        prime_factor = 2
        while current_sum % prime_factor == 0:
            prime_factor += 1
            current_sum //= prime_factor
        prime_factors.append(prime_factor)
        current_sum //= prime_factor
    return prime_factors
