

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # 0 3 6 9 12 15 18 21 24 27 30 33 36 39 42 45 48
    # 1 4 7 10 13 16 19 22 25 28 31 34 37 40 43 46 49
    if not n or n < 0:
        return 0
    count = 0
    for i in range(1, n):
        if i % 7 == 0 or (i % 11 == 0) or (i % 13 == 0):
            count += 1
    return count
