
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
    x1 = interval1[0]
    x2 = interval2[0]
    y1 = interval1[1]
    y2 = interval2[1]

    # When the intervals don't intersect
    if x1 > y2 or x2 < y1:
        return "NO"

    # When the intervals have the same start and end
    if x1 == x2 and y1 == y2:
        return "NO"

    # When the intervals have the same start point but different end points
    if x1 == x2 and y1 != y2:
        return "NO"

    # If the intervals don't have the same start and end
    elif x1 != x2 and y1 != y2:
        return "NO"

    # When the intervals have the same start point and different end points
    elif x1 == x2 and y1 == y2:
        return "YES"
