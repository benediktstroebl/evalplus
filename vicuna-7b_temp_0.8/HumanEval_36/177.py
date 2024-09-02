

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # initialize result
    result = 0
    
    # loop through n times
    for i in range(1, n+1):
        # check for divisibility by 11 and 13
        if i % 11 == 0:
            result += 1
        elif i % 13 == 0:
            result += 1
        else:
            # check if remainder is 7
            if i % 7 == 0:
                result += 1
    
    return result
