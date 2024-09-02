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
    if n < 1:
        raise ValueError("Number should be positive")

    result = []

    def divide(number, divisor):
        if number % divisor == 0:
            result.append(divisor)
            divide(number // divisor, divisor)

    for i in range(2, n):
        divide(n, i)

    return result

