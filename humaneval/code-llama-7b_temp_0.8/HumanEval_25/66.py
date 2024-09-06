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
    if n == 1:
        return [1]
    if n <= 0:
        raise ValueError("Only positive integers are allowed")
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    while n % 3 == 0:
        factors.append(3)
        n //= 3
    divisor = 5
    while n != 1:
        if n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        elif n % divisor == 2:
            factors.append(divisor)
            n = (n // divisor) * divisor + 2
        else:
            divisor += 6 if divisor == 5 else 2
    return factors

