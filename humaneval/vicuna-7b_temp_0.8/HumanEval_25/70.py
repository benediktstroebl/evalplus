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
    prime_factors = []
    for p in range(2, int(n**0.5) + 1):
        if n % p == 0:
            break
    else:
        prime_factors.append(n)
    return prime_factors


n = int(input("Enter a positive integer: "))
prime_factors = factorize(n)
for p in prime_factors:
    print(p)