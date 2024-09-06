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
    # check if n is prime
    if not n % 2:
        return [n]
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i:
            break
    else:
        # if n is prime, factorize it
        factors = []
        for num in range(2, int(n ** 0.5) + 1, 2):
            while n // num == num:
                num += 1
            factors.append(num)
        return factors

