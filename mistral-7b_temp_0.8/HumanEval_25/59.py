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
    # PROBLEM 1:
    # Each integer factor is in the list, and each number in the list is a factor
    # ITERATIVE:
    # 1) Take the number to factorize as a start and a list to store the results
    # 2) If the number to factorize is prime, add it to the list and divide it by the number of times it was found in the list
    # 3) If the number to factorize is not prime, continue to divide by prime factors until it is no longer possible
    # 4) Repeat steps 2 and 3 until the number to factorize is 1
    # RECURSIVE:
    # 1) Take the number to factorize as a start and a list to store the results
    # 2) If the number to factorize is prime, add it to the list and divide it by the number of times it was found in the list
    # 3) If the number to factorize is not prime, continue to divide by prime factors until it is no longer possible
    # 4) Repeat steps 2 and 3 until the number to factorize
