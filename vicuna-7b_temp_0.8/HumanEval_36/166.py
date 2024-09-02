

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # start with 1
    result = 1
    # loop through the numbers 2 to n-1
    for i in range(2, n+1):
        # check for divisibility by 11
        if i % 11 == 0:
            # check for divisibility by 13
            if i % 13 == 0:
                # mark the number as having the fizz or buzz
                result = 7*result + i
        else:
            # mark the number as not having the fizz or buzz
            result = i
    return result
