

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    # check if n is divisible by any number less than n
    for i in range(2, n-1):
        if n % i == 0:
            return i

    # if no divisor is found, return the last number
    return n
