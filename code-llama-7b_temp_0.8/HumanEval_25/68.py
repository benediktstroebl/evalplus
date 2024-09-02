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
    # 1. It's not a prime number, we must divide it with every integer till
    #    it is not prime anymore.
    # 2. Once we divided it to a prime factor, we must divide it with the
    #    prime factor again and again until it becomes 1.
    # 3. The number of times we divided a prime factor is the count of the
    #    prime factor in the factorization.

    # For example,
    # 120 = 2^2 * 3 * 5
    # 120 / 2 = 60
    # 60 / 2 = 30
    # 30 / 3 = 10
    # 10 / 5 = 2
    # 2 / 2 = 1

    # We have 2, 2, 3, 5 in the factorization.

    # Time complexity is O(sqrt(n)).
    # Space complexity is O(1).

    i = 2
    factors = []
    while n > 1:
        while n % i == 0:
            n /= i
            factors.append(i)
        i += 1
    return factors

