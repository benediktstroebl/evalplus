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
    # create helper function to check if number is prime
    def is_prime(n: int) -> bool:
        """
        :return: True if n is prime, False otherwise
        """
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    def factorize_by_trial_division(n: int) -> List[int]:
        """
        Trial division is a simple method of testing if a number is prime by dividing it by all positive integers less than or equal to its square root.
        This function will divide n by all possible numbers less than or equal to sqrt(n) and keep track of how many times each number is a factor.
        If the number is not divisible by any of the numbers, it returns the number of possible factors.
        """
        factors = []
        for i in range(int(n**0.5) + 1):
            if n % i == 0:
                if n != i:
                    for j in range(i, n + 1, i):
                        if n % j == 0:
                            if n != j:
                                factors.append(j)
                                break
        return factors

    # check if n is prime
    if is_prime(n):
        # use trial division method
        return factorize_by_trial_division(n)
    else:
        # use sieve of Eratosthenes algorithm
        # sieve of Eratosthenes is a method for finding all prime numbers up to a given limit.
        # it is more efficient than trial division method but less efficient than other methods.
        n = n - 1
        p = 2
        while p * p <= n:
            if p % n == 0:
                n = p * n + p
            p += 2
        # since n is not prime, it will return a list of all prime factors of n.
        # for example, if n = 14, the result will be [2, 7]
        return [p for p in range(
