

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # Check for divisibility by 11
    if n % 11 == 0:
        return 0
    # Check for divisibility by 13
    if n % 13 == 0:
        return 0
    # Check for divisibility by 3
    if n % 3 == 0:
        return n
    # Check for divisibility by 5
    if n % 5 == 0:
        return n
    # If none of the above conditions are met, we have to count manually
    for i in range(1, n+1):
        # If the number is divisible by 11 and 3 or 13
        if (i % 11 == 0) and (i % 3 == 0 or i % 13 == 0):
            return i
        # If the number is divisible by 7 and 3 or 5
        if (i % 7 == 0) and (i % 3 == 0 or i % 5 == 0):
            return i
        # If the number is divisible by 3 or 5
        if (i % 3 == 0 or i % 5 == 0):
            return i
    # If we reach here, none of the above conditions were met
    return -1