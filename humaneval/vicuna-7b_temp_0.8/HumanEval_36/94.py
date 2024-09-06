

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    d1, d7 = 0, 0
    for i in range(1, n+1):
        if i % 11 == 0:
            d1 += 1
        if i % 13 == 0:
            d7 += 1
        if i % 3 == 0:
            d1 += 1
            if i % 11 == 0:
                d7 += 1
        if i % 5 == 0:
            d1 += 1
            if i % 13 == 0:
                d7 += 1
        if d7 >= n:
            n = d7
    return d1 + d7
