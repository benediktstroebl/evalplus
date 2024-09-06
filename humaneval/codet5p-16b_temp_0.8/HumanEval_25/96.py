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
    for i in range(2, n + 1):
        if i * i > n:
            break
        if n % i == 0:
            count = 0
            while n % i == 0:
                count += 1
                n //= i
            result.append(i)
            result.append(count)
    if n!= 1:
        result.append(n)
    return result

