

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    result = 0
    for i in range(n):
        if (i + 11) % 13 == 0 or (i + 11) % 11 == 0:
            if str(i + 11).find("7") != -1:
                result += 1
    return result

