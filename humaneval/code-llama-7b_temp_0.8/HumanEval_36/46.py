

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # assert n > 0
    # assert type(n) is int
    count = 0
    for x in range(n):
        if x < n and (x % 11 == 0 or x % 13 == 0):
            if str(x).find("7") != -1:
                count += 1
    return count

