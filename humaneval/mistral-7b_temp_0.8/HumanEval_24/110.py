

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # NOTE: for each number you want to test, don't you need to test the numbers before?

    # Assumptions
    if n <= 0:
        return -1

    # Make a guess
    guess = n

    # While the guess is larger than 0 and it doesn't evenly divide n, reduce it by 1 and try again
    while guess > 1 and n % guess != 0:
        guess -= 1

    return guess

