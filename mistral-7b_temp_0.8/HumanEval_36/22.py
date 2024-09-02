

def fizz_buzz(n: int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """
    # YOUR CODE HERE
    # return len([x for x in range(1, n) if (x % 11 == 0 or x % 13 == 0) and x % 10 == 7])
    #or
    cnt = 0
    for i in range(1, n):
        if i % 11 == 0 or i % 13 == 0 and i % 10 == 7:
            cnt += 1
    return cnt
