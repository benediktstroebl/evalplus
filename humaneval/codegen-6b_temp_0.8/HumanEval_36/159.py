

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Note, the solution is simple, but there are rooms for improvements, comments, etc.
    return sum(int(x) % 11 == 7 or int(x) % 13 == 11 for x in str(n))

