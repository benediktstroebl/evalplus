

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    counter = 0
    for i in range(11, n, 11):
        if i % 7 == 0:
            counter += 1
    for i in range(13, n, 13):
        if i % 7 == 0:
            counter += 1
    return counter

