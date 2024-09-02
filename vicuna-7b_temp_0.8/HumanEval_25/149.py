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
    # Combine these two into one function
    # return n // 2 + 1 if n is even
    # return (n - 1) // 2 + 1 if n is odd
    # and check if n is prime and add it to the list if it is
    # return the list

    # Check if n is prime
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return []  # This number is not prime
        return [n]

    # Check if n is even
    if n // 2 == int(n // 2):
        n += 1
        return factorize(n)

    # Check if n is odd
    n -= 1
    return factorize(n)
