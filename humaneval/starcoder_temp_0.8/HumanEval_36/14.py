

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    assert isinstance(n, int) and n > 0
    return sum(7 in str(n) for n in range(1, n) if n % 11 in [0, 1] and n % 13 in [0, 1])
