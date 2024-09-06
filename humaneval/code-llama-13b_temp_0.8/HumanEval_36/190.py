

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    i = 0
    while True:
        if n % 11 == 0 or n % 13 == 0:
            n = str(n)
            if "7" in n:
                i += 1
            else:
                return i
        n += 1
