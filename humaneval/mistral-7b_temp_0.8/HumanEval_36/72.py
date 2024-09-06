

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return sum(
        [int(x) for x in str(i) for i in range(2, n + 1) if (i % 11 == 0 or i % 13 == 0)]
    )
