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

    def is_prime(n: int) -> bool:
        if n < 2:
            return False
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    if n == 1:
        return [1]
    prime_factors = []
    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2

    for i in range(3, n + 1, 2):
        if n % i == 0 and is_prime(i):
            prime_factors.append(i)
            n //= i
    return prime_factors

