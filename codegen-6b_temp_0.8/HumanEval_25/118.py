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
    arr = [0] * (n + 1)
    for i in range(2, n + 1):
        for p in range(2 * i, n + 1, i):
            arr[p] += 1

    result = []
    for i, k in enumerate(arr):
        if k > 0:
            if i == 0:
                result.append(i)
            else:
                result.append(i)
                result.append(i * result[-1])
    return result
