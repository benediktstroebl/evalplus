
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

    # your code here
    # 1, 2, 3, 4
    # 2, 4, 6, 8
    # 2, 3
    # 2, 3, 4

    # 2, 3
    # 1, 2, 3, 4

    # 2, 3
    # 1, 2, 3

    # 2, 3, 4
    # 1, 2, 3

    # 2, 3, 4, 5
    # 1, 2, 3, 4

    # 3, 5, 7
    # 1, 2, 3, 4, 5, 6, 7, 8, 9

    # 3, 6, 9, 12
    # 1, 3, 5, 7, 9, 11, 13, 15
    # 1, 3, 5, 7, 9, 11
    # 3, 6, 9, 12, 15, 18, 21, 24, 27
    # 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49, 51, 53, 55, 57, 59

    # a1, a2 = interval1
    # b1, b2 = interval2

    # if a1 > b2 or b1 > a2:
    #     return "NO"

    # max_start = max(a1, b1)
    # min_end = min(a2, b2)

    # return "YES" if min_end - max_start + 1 == 1 else "NO"
