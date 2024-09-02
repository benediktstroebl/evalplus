

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
    i = 0
    fizz = 0
    while i < n:
        if i % 11 == 0 or i % 13 == 0:
            if i % 7 == 0:
                fizz += 1
        i += 1
    return fizz
