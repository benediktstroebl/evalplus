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
    factors = []
    # step 1: compute factors of n
    # get the first factor (the greatest common divisor is 1)
    count_of_divisors = 0
    divisor = n % 2
    while divisor != 1:
        count_of_divisors += 1
        divisor = n % divisor
    factors.append(n // count_of_divisors)

    # step 2: search for the next factor
    # while the count of divisors of n is less than 2
    #       discover the smallest factor, e.g. 2
    #       try to reduce the current divisor to reach the first factor, e.g. 4
    #       discover the smallest factor, e.g. 4
    #       divide n by the new divisor, n = 4
    #       add the previous count of divisors to the count_of_divsors, e.g. divisor_count = 2
    #       recalculate the new divisor
    #       increment the count of divisors by 1, e.g. divisor_count += 1
    #       add the new divisor to the factors, e.g. factors.append(divisor)
    count_of_divisors = 1
    divisor = 2
    while count_of_divisors < 2:
        divisor_count = 1
        divisor = 2
        while divisor_count < count_of_divisors:
            if n % divisor == 0:
                divisor_count += 1
                divisor = n // divisor
            else:
                divisor += 1
        count_of_divisors = divisor_count
        factors.append(divisor)

    return factors

