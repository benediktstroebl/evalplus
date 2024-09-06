

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    s = 0
    if n < 7:
        return s
    for i in range(7, n):
        if i % 11 == 0 or i % 13 == 0:
            s += (str(i)).count("7")
    return s
