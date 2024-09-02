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
    # Step 1: if number is negative, return error
    # Step 2: if number is 1, return []
    # Step 3: initialize empty list to hold prime factors
    # Step 4: if number is prime, append to list and return
    # Step 5: for i from 2 to sqrt(number)
    # Step 6: if i divides number
    # Step 7: append i to list of factors
    # Step 8: divide number by i and return to Step 4
    # Step 9: if i does not divide number, continue to Step 5

    if n < 1:
        raise ValueError("Cannot factorize negative number")
    if n == 1:
        return []

    factors: List[int] = []

    while n != 1:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                factors.append(i)
                n //= i
                break
        else:
            factors.append(n)
            break

    return factors
