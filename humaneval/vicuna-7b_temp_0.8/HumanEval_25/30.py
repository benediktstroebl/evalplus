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
    # Create list to store factors
    factors = []

    # Check if number is prime
    if n > 1:
        if n % 2 == 0:
            return []
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return []
        # Add number to factors list
        factors.append(n)

    # If number is not prime, then it must be divisible by some number
    for i in range(1, n + 1):
        if n % i == 0:
            # Find smallest divisor
            j = 1
            while n % j == 0:
                j += 1
            # Add smallest divisor to factors list
            factors.append(j)

    # Sort factors
    factors.sort()

    # Initialize result list
    result = []

    # Find product of all factors
    for factor in factors:
        result.append(factor)
        for i in range(len(result)):
            if result[i] % factor == 0:
                return []

    return result
