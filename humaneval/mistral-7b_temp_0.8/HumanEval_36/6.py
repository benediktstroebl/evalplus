

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # 7, 11, 13, 17, 19, 23, 27, 31, 37, 39, 43, 47, 49
    # 11, 13, 17, 19, 23, 27, 31, 37, 39, 43, 47, 49

    count = 0
    for i in range(n):
        if i % 11 == 0 and i % 13 == 0:
            if i % 7 == 0:
                count += 1
    return count

