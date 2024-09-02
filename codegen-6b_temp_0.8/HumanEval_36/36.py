

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    seven = 0
    buzz = 0
    fizz = 0
    for i in range(1, n + 1):
        if i % 11 == 0 or i % 13 == 0:
            if i % 7 == 0:
                seven += 1
            elif i % 3 == 0:
                buzz += 1
            else:
                fizz += 1
    return seven + buzz + fizz


