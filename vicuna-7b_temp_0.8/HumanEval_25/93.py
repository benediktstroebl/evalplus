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
    prime = []
    def is_prime(x: int) -> bool:
        if x <= 1:
            return False
        for i in range(2, int(x**0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    def loop(n: int) -> List[int]:
        for i in range(2, n + 1):
            if is_prime(i):
                prime.append(i)
                if n % i == 0:
                    return [prime]
                if n % i == 1:
                    return [prime, i]
        return [prime]
    result = loop(n)
    result = sorted(result, key=lambda x: x[0])
    return result

