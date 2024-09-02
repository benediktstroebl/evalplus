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
    from math import sqrt
    from itertools import accumulate
    from functools import reduce

    def is_prime(m: int) -> bool:
        if m == 2 or m == 3 or m == 5:
            return True
        if m % 2 == 0 or m % 3 == 0:
            return False
        for i in range(5, int(sqrt(m)) + 1, 6):
            if m % i == 0 or m % (i + 2) == 0:
                return False
        return True

    def seive_of_eratosthenes(n: int) -> List[int]:
        """ Returns list of prime numbers from 2 up to n. """
        primes: List[int] = []
        for num in range(2, n + 1):
            if is_prime(num):
                primes.append(num)
        return primes

    def get_primes_powers(n: int) -> List[int]:
        """ Returns list of prime numbers and powers of their multiplicity in given number. """
        factors = []
        curr_num = n
        for prime in seive_of_eratosthenes(int(sqrt(n) + 1)):
            if curr_num % prime == 0:
                curr_num //= prime
                count = 0
                while curr_num % prime == 0:
                    curr_num //= prime
                    count += 1
                factors.append(prime)
                factors.append(count)
        return factors

    def reduce_list(lst: List[int]) -> List[int]:
        """ Returns list with prime numbers and their multiplicities reduced to the smallest form. """
        while True:
            try:
                i = lst.index(max(lst))
                if i % 2 == 0:
                    j = i - 1
                else:
                    j = i - 2
                if lst[i] < lst[j]:
                    lst[j] = 0
                else:
                    lst[i] = 0
            except ValueError:
                return
