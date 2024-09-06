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
    primes = []
    curr_num = n
    curr_num_index = 0
    while len(primes) == 0 or primes[-1] < curr_num:
        curr_num_index += 1
        curr_num_index_limit = int(curr_num ** 0.5)
        for prime in primes:
            if prime > curr_num_index_limit:
                break
            if curr_num % prime == 0:
                curr_num //= prime
                primes.append(prime)
                break
        if curr_num == 1:
            break
    primes.sort()
    return primes
