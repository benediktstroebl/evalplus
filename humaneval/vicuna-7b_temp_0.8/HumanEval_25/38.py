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
    def is_prime(x: int) -> bool:
        """
        :param x: int
        :return: bool
        """
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    if is_prime(n) or n == 1:
        return [n]

    factors = []
    p = n
    while p != 1:
        while is_prime(p) and p > 1:
            factors.append(p)
            p = p - 1
        p = n // p
        n = n % p

    factors.append(n)
    for i in reversed(range(len(factors))):
        for j in range(i + 1, len(factors)):
            if factors[i] * factors[j] == n:
                factors[i], factors[j] = factors[j], factors[i]
                break

    return factors
