

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    n_fizz = 0
    n_buzz = 0
    n_7 = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0:
            n_buzz += 1
        elif i % 7 == 0:
            n_7 += 1
        else:
            n_fizz += 1
    return n_fizz + n_buzz + n_7
