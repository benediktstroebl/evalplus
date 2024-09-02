

def skjkasdkd(lst):
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    For lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] the output should be 10
    For lst = [1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1] the output should be 25
    For lst = [1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3] the output should be 13
    For lst = [0,724,32,71,99,32,6,0,5,91,83,0,5,6] the output should be 11
    For lst = [0,81,12,3,1,21] the output should be 3
    For lst = [0,8,1,2,1,7] the output should be 7
    """
    if len(lst) == 0:
        return 0
    for n in range(len(lst)):
        if  n < 2:
            continue
        if n > 3 and (n % 2 == 0 or n % 3 == 0):
            continue
        if n > 5 and (n % 5 == 0 or n % 7 == 0):
            continue
        if n > 7 and (n % 7 == 0 or n % 11 == 0):
            continue
        if n > 13 and (n % 13 == 0 or n % 17 == 0):
            continue
        if n > 17 and (n % 17 == 0 or n % 19 == 0):
            continue
        if n > 19 and (n % 19 == 0 or n % 23 == 0):
            continue
        if n > 23 and (n % 23 == 0 or n % 29 == 0):
            continue
        if n > 29 and
