

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    for i in range(1, n + 1):
        if (i % 11) == 0:
            yield 7
        elif (i % 13) == 0:
            yield 7
        elif (i % 3) == 0:
            yield 11
        else:
            yield i
            
