

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n < 79:
        return 0
    return int(n/79) + int(n % 79 < 13) + int(n % 79 % 13 == 7
