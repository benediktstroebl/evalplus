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
    # check if n is prime
    if n == 1:
        return [n]
    elif n % 2 == 0:
        return []
    elif n % 3 == 0:
        return []
    elif n % 2 == 1:
        for num in factorize(n//2):
            if n % num == 0:
                return []
        return [n//2]
    else:
        for num in factorize(n//2):
            for i in range(3, int(n**0.5) + 1, 2):
                if n % (num * i) == 0:
                    return []
        return [2]

