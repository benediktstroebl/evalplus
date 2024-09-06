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
    primes = [2, 3, 5]
    res = []
    for i in range(len(primes)):
        curr_prime = primes[i]
        count = 0
        while n % curr_prime == 0:
            count += 1
            n = n // curr_prime
        if count > 0:
            res.append(curr_prime)
    while n > 1:
        for j in range(len(primes)):
            curr_prime = primes[j]
            if n % curr_prime == 0:
                res.append(curr_prime)
                n = n // curr_prime
                break
        if n > 1:
            primes.append(n)
            res.append(n)
            n = 1
    return res

