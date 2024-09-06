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
    cur_num = n
    cur_prime = 2
    while cur_num != 1 and cur_prime * cur_prime <= cur_num:
        if cur_num % cur_prime == 0:
            result.append(cur_prime)
            cur_num //= cur_prime
        else:
            cur_prime += 1
    if cur_num != 1:
        result.append(cur_num)
    return result

