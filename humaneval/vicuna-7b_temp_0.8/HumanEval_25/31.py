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
    def powsum(i: int, factors: List[int]) -> int:
        """Check if n is divisible by the product of all factors"""
        return 0
    for num in range(1, n + 1):
        if n % num == 0:
            # n is divisible by all numbers from 1 to num
            for factor in factors:
                if num // factor == n // factor:
                    return factor, num // factor
        # if n is divisible by some number, it can't be divisible by any smaller number
        factors.append(num)
    return factors[:]

