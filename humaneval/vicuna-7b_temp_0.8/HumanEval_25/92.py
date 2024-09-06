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
        """
        Returns True if n is prime, False otherwise.
        """
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def get_factors(n: int) -> List[int]:
        """
        Return list of prime factors of given integer n.
        """
        if not is_prime(n):
            return [n]
        factors = []
        while n > 1:
            p = n
            while p > 1 and is_prime(p):
                p = p - 1
            factors.append(p)
            n = n // p
        return factors

    factors = get_factors(n)
    result = []
    for factor in factors:
        count = 1
        while count * count <= n:
            count *= factor
        result.append(count)
    return result

