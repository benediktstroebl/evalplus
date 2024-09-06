

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    count = 0
    for i in range(n):
        if 11 * i in range(n):
            if 7 in str(11 * i):
                count += 1
        if 13 * i in range(n):
            if 7 in str(13 * i):
                count += 1
    return count

