

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    d = {7: 0, 11: 1, 13: 1, 19: 1, 37: 2, 43: 2, 47: 2, 99: 3}
    count = 0
    for i in range(n):
        if i % 11 == 0:
            count += d[7]
        if i % 13 == 0:
            count += d[13]
        if i % 19 == 0:
            count += d[19]
        if i % 37 == 0:
            count += d[37]
        if i % 43 == 0:
            count += d[43]
        if i % 47 == 0:
            count += d[47]
        if i % 99 == 0:
            count += d[99]
    return count
