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
    n_lst = list()
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            n_lst.append(i)
            if n // i == i:
                n_lst.append(i)
            else:
                n_lst.append(n // i)
                n_lst.append(i)
    if n_lst == []:
        n_lst.append(n)
    return n_lst
