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
    while n > 1:
        if n % 2 == 0:
            result.append(2)
            n //= 2
        else:
            candidate = 3
            while candidate ** 2 <= n:
                if n % candidate == 0:
                    result.append(candidate)
                    n //= candidate
                else:
                    candidate += 2
            if n > 1:
                result.append(n)
                n = 1
    return result

