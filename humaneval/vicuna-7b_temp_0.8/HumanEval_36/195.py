

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # 100 is the smallest number that can be divided by 11 and 13,
    # so if the number is divisible by both, then the number is less than 100
    # and will not have a 7 in it.
    return n % 100 != 7
