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
    # write your code here
    if n < 0 or n > 100:
        return "Invalid input"
    factor = []
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            if n % i == 0 and n % j == 0:
                factor.append(i*j)
                break
    if not factor:
        return "No prime factors found"
    return list(map(lambda x: x if x <= n else x*2, factor))

