

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    d = 1
    s = 1
    while n > 0:
        for i in range(s, n+1, d):
            n -= i
        d *= 11
        s *= 13
        d *= 11
        s *= 13
    
    return n