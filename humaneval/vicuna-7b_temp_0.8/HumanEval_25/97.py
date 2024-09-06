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
    def is_prime(n: int) -> bool:
        """
        :param n: int
        :return: boolean
        """
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 == 0:
            return False
        else:
            for i in range(3, int(n ** 0.5) + 1, 2):
                if n % i == 0:
                    return False
            return True
    
    factors = []
    for num in range(1, n + 1):
        if is_prime(num):
            factors.append(num)
    factors = sorted(factors)
    while len(factors) > 1:
        i = 0
        while factors[i] * factors[i + 1] <= n and i < len(factors) - 1:
            i += 1
        if factors[i] * factors[i + 1] > n:
            j = i + 1
            while j < len(factors) and factors[j] * factors[j + 1] == n:
                j += 1
            if j > i:
                factors.pop(j)
                i += 1
        else:
            factors.pop(i)
    return factors

