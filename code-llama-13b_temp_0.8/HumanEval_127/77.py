
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
    # Write your code here
    # make sure start1 <= end1
    if interval1[0] > interval1[1]:
        tmp = interval1[0]
        interval1[0] = interval1[1]
        interval1[1] = tmp

    if interval2[0] > interval2[1]:
        tmp = interval2[0]
        interval2[0] = interval2[1]
        interval2[1] = tmp

    start1, end1 = interval1
    start2, end2 = interval2

    if start1 <= start2 <= end1:
        start = start2
    elif start2 <= start1 <= end2:
        start = start1
    else:
        return "NO"

    if start1 <= end2 <= end1:
        end = end2
    elif start2 <= end1 <= end2:
        end = end1
    else:
        return "NO"

    length = end - start + 1
    if length <= 1:
        return "NO"
    elif length == 2:
        return "NO"
    else:
        i = 2
        while i * i < length:
            if length % i == 0:
                return "NO"
            i += 1
        return "YES"

