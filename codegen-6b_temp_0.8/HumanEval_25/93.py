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
    # Number of factors each number has
    factors_count = [0] * (n + 1)

    for num in range(2, n + 1):
        factor = 2
        # Extra check in case of 1
        while num % factor != 0:
            factor += 1

        # Increment number of factors for each factor
        factors_count[num] = factors_count[factor] + 1

        # Decrement number of factors for each factor
        factors_count[factor] -= 1

        if factors_count[factor] == 0:
            factor += 1

    # Modify each factor to have right prime
    factors = []
    for num, num_factors in enumerate(factors_count):
        while num_factors > 0:
            factors.append(num)
            num_factors -= 1

    return factors

