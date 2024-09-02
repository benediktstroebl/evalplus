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

    result = []
    if n == 1:
        return result
    else:
        for x in range(1, n + 1):
            if n % x == 0:
                if x not in result:
                    result.append(x)
                    result.append(int(n / x))
        return result

