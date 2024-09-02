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
    # Create a list to store prime factors
    factors = []
    # Keep track of current prime factor
    current_factor = 1
    # Iterate through all numbers less than n
    for i in range(1, n + 1):
        # Check if current factor is prime
        if (i % 1) == 0:
            # If it is not prime, add it to the list and continue with next iteration
            factors.append(i)
            continue
        # If it is prime, check if it divides i
        while i % current_factor == 0:
            # If it does not divide, add current factor to the list and update current factor
            factors.append(current_factor)
            current_factor += 1
        # If it divides, add i to the list and update current factor
        factors.append(i)
        current_factor += 1
    # Return the list of prime factors
    return factors

