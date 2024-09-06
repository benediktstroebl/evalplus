

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # handle special case of 1
    if n == 1:
        return 1
    # handle special case of n being a multiple of 3
    if n % 3 == 0:
        return 0
    # handle special case of n being a multiple of 5
    if n % 5 == 0:
        return 0
    # handle general case
    # iterate over numbers less than or equal to n
    # check if n is divisible by 3
    # if it is, return 0
    # if it isn't, check if n is divisible by 5
    # if it is, return 0
    # if it isn't, check if n is divisible by 11
    # if it is, return 1
    # if it isn't, check if n is divisible by 13
    # if it is, return 1
    # if it isn't, return the next number that is divisible by 7
    # and continue until the number is 0
    # or until the number is greater than n
    # if the number is 0, return 0
    # if the number is greater than n, return 1
    for i in range(1, n+1):
        if i % 3 == 0:
            return 0
        if i % 5 == 0:
            return 0
        if i % 11 == 0:
            return 1
        if i % 13 == 0:
            return 1
        if i % 7 == 0:
            return 1
    return 0
