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
    # Make sure input number is positive
    if not n > 0:
        return []

    # Initialize list of factors with length of 1
    factors = [1]

    # Try all possible divisors of n
    for d in range(1, n + 1):
        if not n % d:
            # Add d as a factor and increment the count for each time it appears
            for i in range(d - 1, max(0, n // d - 1), -1):
                factors.append(d)
                for j in range(d - 1, max(0, n // d - j - 1), -1):
                    factors.append(j * d)
                    break

    return factors
