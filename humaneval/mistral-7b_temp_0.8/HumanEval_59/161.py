

def largest_prime_factor(n: int):
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """

    # 1. Pseudocode:
    # Iterate through all numbers from 2 up to n-1
    # If the number is a factor of n, then it is a prime factor.
    # If it's not, then just skip it.
    # Keep track of the highest prime factor.
    # Keep track of the prime factor you just found.
    # Once you get to the end of the list, return the highest prime factor.

    # 2. Data structure:
    # A list of numbers from 2 to n-1.
    # A variable to keep track of the highest prime factor.
    # A variable to keep track of the prime factor you just found.

    # 3. Algorithm:
    # Iterate through the list of numbers, and check if the number is a factor of n.
    # If it is, then update the highest prime factor and set the prime factor you just found to n.
    # If it isn't, then just move on to the next number.
    # Once you get to the end of the list, return the highest prime factor.

    #
