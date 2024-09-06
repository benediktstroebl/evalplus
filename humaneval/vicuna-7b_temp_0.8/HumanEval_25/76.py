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
    # Preconditions
    assert 2 <= n <= 100, "Input number must be in the range of 2 to 100"
    
    # Perform prime factorization of n
    p = 2
    while p <= n:
        while n % p == 0:
            p += 1
        n //= p
    
    # Return list of prime factors
    factors = []
    while p <= n:
        factors.append(p)
        p += 1
    
    # Sort factors in ascending order
    factors = sorted(factors, reverse=False)
    
    # Return list of prime factors
    return factors

