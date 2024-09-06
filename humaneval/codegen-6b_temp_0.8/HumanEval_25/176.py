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
    while n % 2 == 0:
        result.append(2)
        n //= 2

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    while n > 1:
        if is_prime(n):
            result.append(n)
            break
        i = 3
        while n % i != 0:
            i += 2

        while n % i == 0:
            result.append(i)
            n //= i

    return result

