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
    factorization = []
    number = 2
    while number <= n:
        for i in range(number):
            if n % number == 0:
                factorization.append(number)
                n /= number
                break
        number += 1
    factorization.append(n)
    return factorization
