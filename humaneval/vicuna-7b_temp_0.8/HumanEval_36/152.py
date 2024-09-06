

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # If n is divisible by 11 or 13, return 0
    if n % 11 == 0 or n % 13 == 0:
        return 0
    # For n > 0, fizz = n, buzz = n + 1
    while n > 0:
        fizz = n % 11
        n = n // 11
        buzz = n + 1
        # If fizz is 7, return 2
        if fizz == 7:
            return 2
        # If fizz is 11, return 1
        if fizz == 11:
            return 1
        # If buzz is 13, return 3
        if buzz == 13:
            return 3
        # If fizz and buzz are both 1, return 4
        if fizz == 1 and buzz == 1:
            return 4
        # If fizz is 11 and buzz is 13, return 2
        if fizz == 11 and buzz == 13:
            return 2
        # If fizz is 13 and buzz is 11, return 4
        if fizz == 13 and buzz == 11:
            return 4
        # If both fizz and buzz are 7, return 0
        if fizz == 7 and buzz == 7:
            return 0
        # If fizz is 1 and buzz is 13, return 3
        if fizz == 1 and buzz == 13:
            return 3
        # If fizz is 13 and buzz is 1, return 4
        if fizz == 13 and buzz == 1:
            return 4
        # If fizz is 11 and buzz is 7, return 2
        if fizz == 11 and buzz == 7:
            return 2
        # If fizz is 7 and buzz is 11, return 2
        if fizz == 7 and buzz == 11:
            return 2
