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
    # Check if input number is prime
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return []
        # Factorize number
        result = []
        for i in range(1, n):
            if n // i == 0:
                j = n // i
                result.append(i * j)
                while j > 1:
                    if n % j == 0:
                        break
                    j = j // i
                    result.append(j)
        return result
    return []

