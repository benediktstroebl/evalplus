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
    def prime_factors(n):
        # check if the number is divisible by 2 and add it to the factors list
        factors = [2] if n % 2 == 0 else []
        # the loop will run until we get the number itself
        while n % 2 == 0:
            n //= 2
        # loop to iterate from 3 to sqrt(n)
        for i in range(3, int(n**0.5) + 1, 2):
            # check if the number is divisible by i and add it to the factors list
            if n % i == 0:
                factors.append(i)
                while n % i == 0:
                    n //= i
        # if n != 1 it means that there is prime number which not divisible by 2
        # for example 70 has prime factorization 2 x 5 x 7
        if n > 2:
            factors.append(n)
        return factors

    # initialize a list to store prime factors
    factors = []
    # make a copy of the original number and iterate from 2 to the number
    n_copy = n
    for i in range(2, n + 1):
        # prime_factors(n) will return a list of prime factors for given number
        # let's say prime_factors(70) = [2, 5, 7]
        # if the number is prime, prime_factors(70) will return list with one element, that is 70 itself
        if prime_factors(i) == [i]:
            factors.append(i)
        # if we found a factor of n, we will append it to the list,
        # and remove it from the n_copy variable to iterate with
        # let's say n_copy = 140, i = 2
        # 140 // 2 = 70
        # factors = [2]
        # n_copy = 70
        while n_copy % i == 0:
            factors.append(i)
            n_copy //= i
    return factors

