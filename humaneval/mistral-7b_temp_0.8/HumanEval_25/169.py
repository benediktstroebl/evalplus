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
        """ Return True if given number is prime
        >>> is_prime(7)
        True
        >>> is_prime(13)
        True
        >>> is_prime(9)
        False
        >>> is_prime(19)
        True
        """
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    factors: List[int] = []
    current_factor: int = 2

    while n > 1:
        if is_prime(current_factor):
            factors.append(current_factor)
            while n % current_factor == 0:
                n //= current_factor
        current_factor += 1

    return factors

