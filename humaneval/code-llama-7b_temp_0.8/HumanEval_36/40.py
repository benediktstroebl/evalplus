

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    counter = 0
    for x in range(1, n):
        if (x % 11 == 0 or x % 13 == 0) and "7" in str(x):
            counter += 1
    return counter

