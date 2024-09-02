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
        Function to check if a number is prime
        """
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factors(n: int) -> List[int]:
        """
        Function to find all factors of a number
        """
        factors = []
        while n > 1:
            if is_prime(n) and n % 2 == 0:
                n = n / 2
            elif is_prime(n) and n % 3 == 0:
                n = n * 3 + 1
            else:
                factors.append(n)
                n = 1
        return factors

    factors_of_n = factors(n)
    prime_factors = []
    for factor in factors_of_n:
        if factor != 1:
            for i in range(1, len(prime_factors)):
                if prime_factors[i] * prime_factors[i - 1] == factor:
                    prime_factors.insert(i, 1)
                    break
            else:
                prime_factors.append(1)
    return prime_factors
