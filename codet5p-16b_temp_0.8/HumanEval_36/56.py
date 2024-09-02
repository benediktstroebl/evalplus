

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
    for i in range(1, n):
        if 7 % i == 0 and 11 % i == 0 or 13 % i == 0:
            counter += 1
    return counter
