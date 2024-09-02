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
    factors = []
    if n % 2 == 0:
        factors.append(2)
        x = n + 1
    else:
        x = n
    while x % 2 == 0:
        x /= 2
    if x != 1:
        factors.append(int(x))
    for i in range(3, int(x ** 0.5 + 1), 2):
        while x % i == 0:
            x /= i
            factors.append(i)
    if x > 2:
        factors.append(int(x))
    return factors

