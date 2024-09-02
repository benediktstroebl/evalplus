

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n < 10:
        if n % 11 == 0 or n % 13 == 0:
            return 1
        else:
            return 0
    else:
        if n % 11 == 0:
            return 1 + fizz_buzz(n // 11)
        elif n % 13 == 0:
            return 1 + fizz_buzz(n // 13)
        else:
            return fizz_buzz(n // 10)

