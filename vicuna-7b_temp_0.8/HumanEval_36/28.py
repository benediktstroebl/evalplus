

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n < 0 or not n % 11 or not n % 13:
        return 0
    else:
        x = 0
        for i in range(n // 11):
            x += 1
        for i in range(n // 13):
            x += 1
        for i in range(n - (x // 11)):
            x += 1
        for i in range((x // 13) + 1):
            x += 1
        return x
