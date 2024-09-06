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
    if n < 1:
        raise ValueError("Number should be greater than zero")

    def _factorize(n: int, count: int = 0) -> List[int]:
        if n == 1:
            return [n]
        i = 2
        factors = []
        while i * i <= n:
            while n % i == 0:
                factors.append(i)
                n //= i
            i += 1
        factors.append(n)
        if count:
            return factors * count
        return factors

    def _factorize_nondec(n: int) -> List[int]:
        if n < 1:
            raise ValueError("Number should be greater than zero")

        def _nondec_for_n(n: int) -> int:
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n % 2 == 0:
                return _nondec_for_n(n // 2) + 1
            return _nondec_for_n(3 * n + 1) + 1

        if n < 4:
            return [n]

        if n % 2 == 0:
            return _factorize_nondec(n // 2) + [2]
        return _factorize_nondec(_nondec_for_n(n - 1) + 1) + [n - 1]

    factors = _factorize_nondec(n)
    if len(factors) == 1:
        return factors
    return factors + [n // f for f in factors]

