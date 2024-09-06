
def intersection(interval1, interval2):
    """You are given two intervals,
    where each interval is a pair of integers. For example, interval = (start, end) = (1, 2).
    The given intervals are closed which means that the interval (start, end)
    includes both start and end.
    For each given interval, it is assumed that its start is less or equal its end.
    Your task is to determine whether the length of intersection of these two 
    intervals is a prime number.
    Example, the intersection of the intervals (1, 3), (2, 4) is (2, 3)
    which its length is 1, which not a prime number.
    If the length of the intersection is a prime number, return "YES",
    otherwise, return "NO".
    If the two intervals don't intersect, return "NO".


    [input/output] samples:
    intersection((1, 2), (2, 3)) ==> "NO"
    intersection((-1, 1), (0, 4)) ==> "NO"
    intersection((-3, -1), (-5, 5)) ==> "YES"
    """
    # Your code here
    # Note that you can use functions from the set below to solve this problem
    # set()
    # list()
    # int()
    # str()
    # float()
    # len()
    # max()
    # min()
    # range()
    # map()
    # pow()
    # sum()
    # abs()
    # round()
    # divide()
    # multiply()
    # return ""

    if interval1[0] == interval1[1]:
        return "NO"

    if interval2[0] == interval2[1]:
        return "NO"

    if interval1[1] < interval1[0]:
        return "NO"

    if interval2[1] < interval2[0]:
        return "NO"

    if interval1[0] < interval2[0]:
        lower = interval2[0]
        higher = interval1[1]
    elif interval1[0] > interval2[0]:
        lower = interval1[0]
        higher = interval2[1]
    else:
        lower = interval1[0]
        higher = max(interval1[1], interval2[1])

    if lower > higher:
        return "NO"

    diff = higher - lower
    if diff == 1:
        return "NO"

    if diff == 2:
        return "YES"

    for i in range(3, int(diff/2) + 1, 2):
        if diff % i == 0:
            return "NO"

    return "YES"
