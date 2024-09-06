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
    count = 1
    for num in range(1, int(n ** 0.5) + 1):
        if n % num == 0:
            result.append(num)
            count *= num
            n //= num
    result.append(n)
    result.sort()
    return result * count

