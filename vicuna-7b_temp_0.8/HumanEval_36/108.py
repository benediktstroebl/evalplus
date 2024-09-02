

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # initialize the result list
    results = []
    # iterate over the integers less than n
    for i in range(1, n+1):
        # check if i is divisible by 11
        if i % 11 == 0:
            # check if i is divisible by 13
            if i % 13 == 0:
                # if both conditions are true, increment the result list
                results.append(i)
        # if i is not divisible by 11 or 13, add 1 to the result list
        else:
            results.append(i + 1)
    return results
