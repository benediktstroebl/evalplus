

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # if n < 7:
    #     return 0
    # num = 1
    # counter = 0
    # while num < n:
    #     if num % 11 == 0 or num % 13 == 0:
    #         if num % 10 == 7:
    #             counter += 1
    #     num += 1
    # return counter
    counter = 0
    if n < 7:
        return counter
    for i in range(7, n):
        if i % 11 == 0 or i % 13 == 0:
            if i % 10 == 7:
                counter += 1
    return counter

