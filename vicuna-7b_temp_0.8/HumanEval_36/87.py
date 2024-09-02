

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check if n is divisible by 11, 13 or 7
    if n % 11 == 0:
        return 0
    elif n % 13 == 0:
        return 0
    elif n % 7 == 0:
        return 0
    else:
        # Number is not divisible by 11, 13 or 7
        # so it is divisible by 3
        return 1