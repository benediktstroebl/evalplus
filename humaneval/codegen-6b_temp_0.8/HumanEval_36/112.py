

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    c = 0
    for i in range(n):
        if (i+1) % 11 == 0:
            c += (i+1) // 11
        elif (i+1) % 13 == 0:
            c += (i+1) // 13
        elif (i+1) % 7 == 0:
            c += (i+1) // 7
    return c
