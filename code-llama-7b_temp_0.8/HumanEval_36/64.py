

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # return sum([int(x.count('7')) for x in map(str, range(n)) if x % 11 == 0 or x % 13 == 0])
    ret = 0
    for x in range(n):
        if x % 11 == 0 or x % 13 == 0:
            if str(x).count('7') > 0:
                ret += 1
    return ret

