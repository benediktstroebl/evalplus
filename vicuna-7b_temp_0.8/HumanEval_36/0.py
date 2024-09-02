

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    d7 = 0
    d11 = 0
    d13 = 0
    for i in range(1, n+1):
        if i % 11 == 0:
            d11 += 1
        elif i % 13 == 0:
            d13 += 1
        elif i % 3 == 0:
            d7 += 1
        else:
            d7 += 1 if i % 5 == 0 else d11 += 1 if i % 7 == 0 else d13 += 1
    return d7 + d11 + d13
