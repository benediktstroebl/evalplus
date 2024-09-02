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
    factor_list = []
    prime_factors, max_iters = [2, ], 0

    if n == 1:
        return factor_list

    while n > 1:
        # Keep adding factors while n is above 1
        max_iter = max_iters + 1
        for prime in prime_factors:
            while n % prime == 0:
                max_iter += 1
                n /= prime

        # If no factor found, factor is itself
        if max_iter == max_iters:
            factor_list.append(n)
            break

        # Add the new factor to list of factors
        max_iters = max_iter
        prime_factors.append(n)

    return factor_list

