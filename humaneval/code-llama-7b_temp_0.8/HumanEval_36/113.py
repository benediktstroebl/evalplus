

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    assert n > 0
    res = 0
    for x in range(1, n):
        if x % 11 == 0 or x % 13 == 0:
            while x > 0:
                if x % 10 == 7:
                    res += 1
                x //= 10
    return res

