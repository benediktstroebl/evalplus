

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n <= 0:
        raise ValueError("n should be a positive integer")
    if n <= 20:
        return 0
    return fizz_buzz(n // 3) * (n // 3) + fizz_buzz(n // 5) * (n // 5) + fizz_buzz(n // 15) * (n // 15
