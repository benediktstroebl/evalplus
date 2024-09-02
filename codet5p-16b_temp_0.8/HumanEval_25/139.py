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

    assert isinstance(n, int), "Factorization of non-integer value"
    assert n > 0, "Factorization of negative number"
    prime = [2, 3, 5, 7]  # sorted prime numbers
    factor = []
    while prime:
        p = prime.pop()
        if n % p:
            factor.append(p)
            continue
        q = n // p
        while not n % p:
            n //= p
            factor.append(p)
        if prime:
            prime.append(q)
        else:
            factor.append(q)
            break
    return factor

