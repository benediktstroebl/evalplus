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
        Check if given number is prime
        """
        if n < 2:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

    prime_factors = []
    n = int(n)
    while n > 1:
        for i in range(2, int(n**0.5) + 1):
            if is_prime(i):
                prime_factors.append(i)
                for j in prime_factors:
                    if j % n == 0:
                        break
                else:
                    break
        n = n // 2
    return prime_factors

