

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    #  71 61 51 41 31 21
    # 51 57 52 53 54 55 56 58 59
    # 41 47 42 43 44 45 46 48 49
    # 31 37 32 33 34 35 36 38 39
    # 21 27 22 23 24 25 26 28 29
    # 11 17 12 13 14 15 16 18 19
    # 71 61 51 41 31 21 11
    # 71 67 61 62 63 64 65 66 68 69
    # 51 57 52 53 54 55 56 58 5
