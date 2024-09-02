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
    fact = []
    # set minimum as 2 and start checking as 3
    min = 2
    i = 3  # incrementing as we iterate through numbers of factors
    # while loop will terminate when i is greater than n
    while i <= n:
        # every iteration, one of the prime factors is incremented by 1
        while n % i == 0:
            n = n / i
            fact.append(i)
        # if we reach that point that n is greater than i, we increment i and start iterating
        i += 1
    # if n is greater than 2, we append the prime number
    if n > 2:
        fact.append(n)
    return fact

