

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check for divisibility by 11 and 13
    if n % 11 == 0:
        return 0
    if n % 13 == 0:
        return 0
    # Check for divisibility by 3
    if n % 3 == 0:
        return 1
    # Check for divisibility by 5
    if n % 5 == 0:
        return 1
    # Check for divisibility by both 3 and 5
    if n % 3 == 0 and n % 5 == 0:
        return 2
    # Check for divisibility by 11 and 13
    if n % 11 == 0:
        return 2
    if n % 13 == 0:
        return 2
    # Check for divisibility by 13 and 7
    if n % 13 == 0 and n % 7 == 0:
        return 3
    # Check for divisibility by 11 and 7
    if n % 11 == 0 and n % 7 == 0:
        return 4
    # Check for divisibility by 13 and 11
    if n % 13 == 0 and n % 11 == 0:
        return 4
    # Check for divisibility by 17 and 7
    if n % 17 == 0 and n % 7 == 0:
        return 6
    # Check for divisibility by 25 and 3
    if n % 25 == 0 and n % 3 == 0:
        return 1
    # Check for divisibility by 25 and 5
    if n % 25 == 0 and n % 5 == 0:
        return 1
    # Check for divisibility by 25 and 22
    if n % 25 == 0 and n % 22 == 0:
        return 1
    # Check for divisibility by 25 and 4
    if n % 25 == 0 and n % 4 == 0:
        return 1
    # Check for divisibility by 
