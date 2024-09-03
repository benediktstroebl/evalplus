def skjkasdkd(lst):
    """
    You are given a list of integers.
    The function aims to find the largest prime value in the list and returns the sum of its digits.

    Examples:
    lst = [0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3] 
    the output should be 10
    """
    return sum([x for x in lst if x >= 1 and x % 10 == 0])