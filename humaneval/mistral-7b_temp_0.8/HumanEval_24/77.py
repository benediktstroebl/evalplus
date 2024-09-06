

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # 1. Write a function that takes in an integer n and returns the largest number that divides n evenly.

    # 2. Break out of the loop when divisor >= n
    # 3. Return divisor

    divisor = 2
    while divisor < n:
        if n % divisor == 0:
            return divisor
        divisor += 1

    return divisor

