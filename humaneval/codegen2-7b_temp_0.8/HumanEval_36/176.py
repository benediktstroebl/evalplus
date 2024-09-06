

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    fizz_buzz = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            fizz_buzz += 1
        elif i % 5 == 0:
            fizz_buzz += 1
        elif i % 3 == 0:
            fizz_buzz += 1
    return fizz_
