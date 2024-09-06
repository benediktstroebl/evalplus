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
    # using long multiplication to check if given integer is divisible by any of the numbers from 2 to sqrt(n)
    # if not, then the number is prime, and we return it
    if not n % 2 and not n % 3 and not n % 4 and not n % 5:
        return [n]
    # checking if n is divisible by 6
    if n % 6 == 0:
        # if it is divisible by 6, we know that it is divisible by 2 and 3, so we just check for divisibility by 2 and 3
        if n % 2 == 0:
            return [2]
        if n % 3 == 0:
            return [3]
    # looping from 7 to sqrt(n) and checking if n is divisible by each number
    for i in range(7, int(sqrt(n))+1):
        if n % i == 0:
            # if it is divisible by i, we know that it is also divisible by i-1, so we check for divisibility by i-1
            if n % (i-1) == 0:
                # if it is divisible by i-1, we have found a factor, and we return it
                return [i]
            else:
                # if it is not divisible by i-1, we have found a prime factor, and we add it to the list of factors
                return [i] + factorize(n-n%i)
    # if n is divisible by any number from 7 to sqrt(n), then it has no prime factors, and we return an empty list
    return []

