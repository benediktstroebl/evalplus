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
    factors = []

    def _factorize(n: int, _factorize_result: List[int]):
        if n < 2:
            return _factorize_result
        while n % 2 == 0:
            _factorize_result.append(2)
            n //= 2
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                _factorize_result.append(i)
                while n % i == 0:
                    n //= i
            if i ** 2 > n:
                if n > 1:
                    _factorize_result.append(n)
                break
        if n > 1:
            _factorize_result.append(n)
        return _factorize_result

    factors = _factorize(n, factors)
    return factors

