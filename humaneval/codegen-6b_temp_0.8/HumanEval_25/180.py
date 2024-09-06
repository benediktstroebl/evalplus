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
    factor_list = []

    def is_prime(num: int) -> bool:
        """ Return True if given number is prime and False otherwise """
        if num == 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def get_divisors(num: int) -> List[int]:
        """ Return list of divisors of given number """
        divisors = []
        for i in range(1, num):
            if num % i == 0:
                divisors.append(i)
        return divisors

    def get_factors(num: int) -> List[int]:
        """ Return list of factors of given number in the order from smallest to largest """
        divisors = get_divisors(num)
        factors = []
        for divisor in divisors:
            count = 0
            while num % divisor == 0:
                num /= divisor
                count += 1
            factors.append([divisor, count])
        if num != 1:
            factors.append(num)
        factors.sort(key=lambda item: item[0])
        return factors

    while n > 1:
        if is_prime(n):
            factor_list.append(n)
        else:
            factors = get_factors(n)
            f1, f2 = factors[0][0], factors[1][0]
            if f1 == f2:
                factors[1][0] = factors[0][0] + factors[1][0]
                del factors[0]
            n /= f1
        if n <= 1:
            break
    return factor_list

