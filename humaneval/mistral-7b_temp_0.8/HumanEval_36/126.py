

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    num_sevens = 0
    for x in range(n):
        if x % 11 == 0 or x % 13 == 0:
            if x % 10 == 7 or x % 100 == 7 or x % 1000 == 7 or x % 10000 == 7:
                num_sevens += 1
    return num_sevens

