

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    if n < 79:
        return 0
    else:
        return sum(7 in str(i) and i % 11!= 0 and i % 13!= 0 for i in range(1, n + 1
