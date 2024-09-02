

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if not n % 11 and not n % 13:
        return n - n % 11 - n % 13
    elif n % 13:
        return fizz_buzz(n // 13) + fizz_buzz(n % 13)
    else:
        return fizz_buzz(n % 11)
