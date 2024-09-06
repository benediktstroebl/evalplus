

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    "*** YOUR CODE HERE ***"
    def iter_fizz_buzz(var: int):
        if var == 0:
            return 0
        if var % 11 == 0 or var % 13 == 0:
            return 1 + iter_fizz_buzz(var - 1)
        else:
            return iter_fizz_buzz(var - 1)
    return iter_fizz_buzz(n)

