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
    assert n > 0, 'Input should be positive integer'

    # Replace this code with a while loop.
    # i = 2
    # while i * i <= n:
    #     if n % i == 0:
    #         n //= i
    #         f.append(i)
    #     else:
    #         i += 1

    # Add assertions to test if the result is correct.
    # assert n == 1, 'Input number should be equal to the product of all factors'

    # Replace this code with a while loop.
    # f.sort()

    # Add assertions to test if the result is correct.
    # assert all(f[i] == f[i-1] for i in range(1, len(f))), \
    #     'Prime factors should be listed from smallest to largest'

    return []
