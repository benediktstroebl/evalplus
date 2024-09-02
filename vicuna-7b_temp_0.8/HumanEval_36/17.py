

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Try 11 as the first possibility
    for i in range(n, 1, 11):
        if i % 11 % 3 == 0:
            return 3
    # Try 13 as the second possibility
    for i in range(n, 1, 13):
        if i % 13 % 3 == 0:
            return 3
    # Try 7 as the first possibility
    for i in range(n, 1, 7):
        if i % 7 % 3 == 0:
            return 3
    # Try 11 as the third possibility
    for i in range(n, 1, 11):
        if i % 11 % 3 == 0:
            return 1
    # Try 13 as the third possibility
    for i in range(n, 1, 13):
        if i % 13 % 3 == 0:
            return 1
    # Try 7 as the second possibility
    for i in range(n, 1, 7):
        if i % 7 % 3 == 0:
            return 1
    # Try 11 as the fourth possibility
    for i in range(n, 1, 11):
        if i % 11 % 3 == 0:
            return 1
    # Try 13 as the fourth possibility
    for i in range(n, 1, 13):
        if i % 13 % 3 == 0:
            return 1
    # Try 7 as the third possibility
    for i in range(n, 1, 7):
        if i % 7 % 3 == 0:
            return 2
    # Try 11 as the fifth possibility
    for i in range(n, 1, 11):
        if i % 11 % 3 == 0:
            return 2
    # Try 13 as the fifth possibility
    for i in range(n, 1, 13):
        if i % 13 % 3 == 0:
            return 2
    # Try 
