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
    prime_factors = []
    temp = n
    prime_nums = {2, 3, 5, 7}
    while temp != 1:
        for p in prime_nums:
            if temp % p == 0:
                prime_factors.append(p)
                temp //= p
                break
    return prime_factors

