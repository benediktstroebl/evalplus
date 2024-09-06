

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
    for i in range(1, n):
        if (i % 7 == 0 or str(i).count('7')) and (i % 11 == 0 or str(i).count('11')) and (i % 13 == 0 or str(i).count('13')):
            count += 1
    return count
