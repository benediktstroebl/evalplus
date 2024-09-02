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
    p_factors = [2]
    while n % 2 == 0:
        n //= 2
        p_factors.append(2)
    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            n //= i
            p_factors.append(i)
    if n!= 1:
        p_factors.append(n)
    return p_fact
