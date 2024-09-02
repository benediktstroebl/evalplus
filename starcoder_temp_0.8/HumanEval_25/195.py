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
    if n == 1:
        return [1]
    if n == 0:
        return [0]
    factors = []
    current_number = n
    while current_number > 1:
        divisor = 2
        while current_number % divisor!= 0:
            divisor += 1
        factors.append(divisor)
        current_number /= divisor
    return factors
