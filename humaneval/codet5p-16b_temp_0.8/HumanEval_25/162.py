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

    result = []
    if n % 2!= 0:  # Number is prime
        result.append(n)
    else:
        result.append(2)
        while n % 2 == 0:
            n //= 2
            result.append(2)

    current_number = 3
    while current_number * current_number <= n:
        if n % current_number == 0:
            result.append(current_number)
            n //= current_number
        else:
            current_number += 2

    if n!= 1:
        result.append(n)
    return result
