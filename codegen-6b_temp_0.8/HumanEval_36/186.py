

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # start with an empty list of results
    res = []

    # for each integer between 1 and n
    for i in range(1, n + 1):
        # if the integer is divisible by either 11 or 13
        if i % 11 == 0 or i % 13 == 0:
            # append the result to the results list
            res.append('Fizz Buzz')

        # if the integer is divisible by 11
        elif i % 11 == 0:
            # append the result to the results list
            res.append('Fizz')

        # if the integer is divisible by 13
        elif i % 13 == 0:
            # append the result to the results list
            res.append('Buzz')

        # if none of the above conditions are true
        else:
            # append the result to the results list
            res.append(i)

    # return the total number of results
    return len(res)
    
