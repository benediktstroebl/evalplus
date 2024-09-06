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
    i = 2
    fac_list = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            if i not in fac_list:
                fac_list.append(i)
            else:
                fac_list.remove(i)
    if n > 1:
        fac_list.append(n)
    return fac_list

