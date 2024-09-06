

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
    for i in range(1, n+1):
        if i % 11 == 0:
            d[i] = 0
        elif i % 13 == 0:
            d[i] = 1
        else:
            d[i] = 0
    for i in range(2, n+1):
        if d[i] > 0:
            yield i
            for j in range(i*11, n+1, 11):
                yield j
            for j in range(i*13, n+1, 13):
                yield j
            d[i] = d[i] - 1