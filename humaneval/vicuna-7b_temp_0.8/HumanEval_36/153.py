

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # split the range between fizz and buzz
    fizz_range = (1, 100)
    buzz_range = (11, 100)
    
    # check for each number in the fizz_range
    fizz = 0
    for i in fizz_range:
        if (i % 11 == 0 and i % 13 == 0 or i % 11 == 13 or i % 13 == 11):
            fizz += 1
    
    # check for each number in the buzz_range
    buzz = 0
    for i in buzz_range:
        if (i % 11 == 0 and i % 13 == 0 or i % 11 == 13 or i % 13 == 11):
            buzz += 1
    
    return fizz + buzz
