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
    if n < 2:
        return []
    else:
        prime_factors = []
        for num in range(1, n):
            while num % 2 == 0:
                num = num / 2
            while num % 3 == 0:
                num = num / 3
            while num % 5 == 0:
                num = num / 5
            while num % 7 == 0:
                num = num / 7
                prime_factors.append(num)
        return prime_factors