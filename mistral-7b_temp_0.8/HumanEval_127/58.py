
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
    # 95 % accepted
    s1 = interval1[0]
    e1 = interval1[1]
    s2 = interval2[0]
    e2 = interval2[1]
    if e1 < s2 or e2 < s1:
        return 'NO'
    if e1 >= e2:
        return 'YES'
    if s1 >= e2 or e1 <= s2:
        return 'NO'
    if e1 <= e2:
        return 'YES'

    # 5 % accepted
    s1, e1 = interval1
    s2, e2 = interval2
    if s1 > e2 or e1 < s2:
        return 'NO'
    if s1 > e1 or s2 > e2:
        return 'NO'
    return 'YES'
