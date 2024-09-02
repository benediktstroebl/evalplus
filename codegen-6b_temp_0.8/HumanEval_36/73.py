

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n < 0:
        return 0
    if n % 11 == 0:
        return fizz_buzz(n // 11) + FIZZ_BULL
    elif n % 13 == 0:
        return fizz_buzz(n // 13) + BIZZ_BILL
    elif n % 7 == 0 and n % 5 != 0:
        return fizz_buzz(n // 7) + FIZZ
    else:
        return 0
