

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # 7 appears
    if n % 7 == 0:
        return 0
    # 11 appears
    if n % 11 == 0:
        return 0
    # 7 appears before 11 does
    if n % 7 == 0 and n % 11 == 0:
        return 0
    # 13 appears
    if n % 13 == 0:
        return 0
    # 7 appears after 13 does
    if n % 7 == 0 and n % 13 == 0:
        return 0
    # 11 appears after 13
    if n % 11 == 0 and n % 13 == 0:
        return 0
    # else, return 1
    else:
        return 1