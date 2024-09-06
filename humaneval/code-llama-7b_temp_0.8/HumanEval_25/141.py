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
    factorization = []
    number = n
    i = 2
    while i ** 2 <= number:
        if number % i == 0:
            factorization.append(i)
            number //= i
            i = 2
        else:
            i += 1
    if number > 1:
        factorization.append(number)
    return factorization

