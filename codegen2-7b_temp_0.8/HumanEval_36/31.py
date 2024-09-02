

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return sum(1 for i in range(n+1) if i % 7 in (1, 3) and i % 11 in (0, 2, 4, 6, 8, 10))
