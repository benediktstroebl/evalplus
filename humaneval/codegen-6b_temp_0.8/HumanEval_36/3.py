

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    fizz = buzz = 0
    while n:
        if n % 11 == 0:
            buzz += n // 11
        elif n % 13 == 0:
            fizz += n // 13
        else:
            n -= 1
    return buzz + fizz

