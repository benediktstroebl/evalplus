

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # check if n is divisible by 11 or 13
    if n % 11 or n % 13:
        return n
    
    # if n is not divisible by 11 or 13, return 0
    else:
        return 0
