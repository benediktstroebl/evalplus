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
    # If n is less than 1 then return empty list
    if n < 1:
        return []

    # All primes are greater than 1
    if n == 1:
        return [1]

    # Each time we get a factor, we multiply the number by the factor to get the new number
    # Once we have the number, we run through all the factors and increment their appropriate count
    result = []
    while n is not 1:
        number_to_factor = n
        for i in range(2, n + 1):
            while number_to_factor % i == 0:
                number_to_factor /= i
                result.append(i)
        if number_to_factor == 1:
            break
    return result

