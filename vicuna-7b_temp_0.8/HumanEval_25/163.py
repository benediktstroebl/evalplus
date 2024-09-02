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
    def check(x):
        if x % 2 == 0:
            return False
        else:
            for y in range(3, x+1, 2):
                if x % y == 0:
                    return False
            return True
    factors = [check(n)]
    while len(factors) > 1:
        for x in factors:
            if x == True:
                for y in range(x+1, n+1, 2):
                    if n % y == 0:
                        for z in range(x, y-1, -1):
                            if n % z == 0:
                                x = z
                                break
                        n = y
                        factors = [y]
                        break
                else:
                    n = x
                    factors = [x]
                    break
    return factors

