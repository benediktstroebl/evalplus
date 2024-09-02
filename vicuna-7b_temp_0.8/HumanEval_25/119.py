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
    # check if input is prime
    if n < 2:
        return [n]
    # check if n is prime
    if n > 2:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return [n]
        return [n]
    # check if n is prime and n is less than 2
    # since we have checked if n is prime
    # so we dont need to check again
    return factorize(n//2) + [n//2]

