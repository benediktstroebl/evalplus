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

    if n < 2:
        return []
    elif n == 2:
        return [2]
    elif n == 3:
        return [3]
    factors = [n]
    prime = 2
    while n > 1:
        if n % prime == 0:
            factors.append(prime)
            n = n / prime
        else:
            prime += 1
    return factors
    
    
