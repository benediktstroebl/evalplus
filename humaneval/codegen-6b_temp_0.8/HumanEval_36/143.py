

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n < 1:
        return 0
    else:
        return fizz_buzz(n) + 1 if n % 3 == 0 or n % 5 == 0 else fizz_buzz(n)


from doctest import testmod
