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
        """Check if a number is prime or not"""
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n % 2 != 0:
            return False
        elif n > 2 and n % 3 == 0:
            return False
        else:
            for i in range(4, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
    def get_factors(n: int) -> List[int]:
        """Return list of all factors of given number"""
        factors = []
        while n > 1:
            n = n // 2  # Since n is odd, we can divide it by 2 and get an even number
            factors.append(n)
        while n > 1:
            n = n // 3  # Since n is odd, we can divide it by 3 and get an odd number
            factors.append(n)
        return factors
    factors = get_factors(n)
    prime_factors = []
    for factor in factors:
        while factor > 1:
            if is_prime(factor):
                prime_factors.append(factor)
                for i in range(factor - 1, n + 1):
                    if n % i == 0:
                        break
                else:
                    break
            factor = factor // 2  # Since factor is odd, we can divide it by 2 and get an even number
        else:
            for i in range(factor - 1, n + 1):
                if n % i == 0:
                    break
            else:
                break
    return prime_factors

