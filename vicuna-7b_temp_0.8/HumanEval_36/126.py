

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    d = {}
    for i in range(n):
        if i % 11 == 0:
            d[i] = 7
        elif i % 13 == 0:
            d[i] = 11
        else:
            d[i] = 0
    return sum(d.values())
