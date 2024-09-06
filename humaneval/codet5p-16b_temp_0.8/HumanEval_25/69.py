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
    from itertools import count, islice
    def prime_numbers_generator():
        D = {}  # a dictionary of primed numbers
        yield 2
        for q in islice(count(3), int(sqrt(n) - 1)):
            p = D.pop(q, None)  # get last occuring prime number
            if p is None:
                D[q * q] = q
            else:
                x = q + 2 * p
                while x in D or not (x & 1):
                    x += 2 * p
                D[x] = p
                yield x
    a = list(prime_numbers_generator())
    b = []
    for i in range(len(a)):
        if n % a[i] == 0:
            b.append(a[i])
            n = n // a[i]
    return b[::-1]

