
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
    start1, end1 = interval1
    start2, end2 = interval2

    if start1 > end1 or start2 > end2:
        return "NO"

    if start1 == end1 and start2 == end2:
        return "YES"

    if end1 < start2:
        return "NO"

    if end2 < start1:
        return "NO"

    intersection = max(start1, end1)
    for i in range(len(start1) - 1):
        if start1[i] == end1[i] and start1[i + 1] != end1[i + 1]:
            intersection = min(intersection, start1[i + 1])

    for i in range(len(start2) - 1):
        if start2[i] == end2[i] and start2[i + 1] != end2[i + 1]:
            intersection = max(intersection, start2[i + 1])

    if end1 < intersection or end2 < intersection:
        return "NO"

    if intersection > max(start1, end1, start2, end2):
        return "YES"

    return "NO"
