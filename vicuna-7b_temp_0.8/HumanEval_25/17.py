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
        """ Returns True if n is prime, False otherwise."""
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n: int) -> List[int]:
        """ Returns list of prime factors of n. """
        factors = []
        while n > 1:
            if is_prime(n):
                factors.append(n)
                n = n - 1
            else:
                n = n // 2
        return factors

    n = int(n)
    if n == 1:
        return [n]
    while n > 1:
        n = n // 2
        factors = get_factors(n)
        for i in factors:
            for j in factors:
                if i * j == n:
                    n = n - i * j
                    break
        if n == 1:
            break
    return factors

