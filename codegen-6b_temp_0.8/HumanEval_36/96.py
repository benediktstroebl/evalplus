

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    "*** YOUR CODE HERE ***"
    p1 = 0
    p2 = 0
    for _ in range(1, n+1):
        if (_ % 11 == 0) or (_ % 13 == 0):
            p2 += 1
        elif _ % 7 == 0:
            p1 += 1
    return p1+p2
