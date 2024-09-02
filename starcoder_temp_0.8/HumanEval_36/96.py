

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    return sum(map(lambda x: len(x) == 3 and (x[0] == '7' or x[1] == '7' or x[2] == '7'), [str(x) for x in range(n) if x % 11 == 0 or x % 13 == 0]))
