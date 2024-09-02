

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
        raise ValueError("Integers less than 0 are not allowed")
    return sum(c in "7" for c in str(n)) + sum(c in "13" for c in str(n))
