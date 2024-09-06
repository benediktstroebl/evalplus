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
    # if number is 0 or 1, return [1]
    if n == 0 or n == 1:
        return [1]

    # create list to store current prime factors
    current_factors = [n]
    # for each number that is less than or equal to sqrt(n)
    for i in range(1, int(n**0.5) + 1):
        # if the number is not a prime, we need to find its factors
        while i % i == 0:
            # if the number has a factor greater than its sqrt, we know that the number is not prime
            if i != i**2:
                # add it to the current list of factors
                current_factors.append(i)
            i += 1
        # if the number is a prime, add it to the list of prime factors
        if i > 1:
            current_factors.append(i)

    # sort the factors
    current_factors = sorted(current_factors)
    # return the list of prime factors in the order from smallest to largest
    return current_factors
