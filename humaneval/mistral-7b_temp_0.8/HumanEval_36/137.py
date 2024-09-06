

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    cnt = 0
    for x in range(n):
        if not x % 11 and x % 13:
            cnt += 1
        elif not x % 13 and x % 11:
            cnt += 1
        elif not x % 11 and not x % 13:
            cnt += 2
    return cnt

