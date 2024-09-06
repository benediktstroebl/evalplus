
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

    assert isinstance(interval1, tuple), "Input is not a tuple"
    assert isinstance(interval2, tuple), "Input is not a tuple"
    assert len(interval1) == 2, "Interval1 does not have 2 elements"
    assert len(interval2) == 2, "Interval2 does not have 2 elements"
    assert interval1[0] <= interval1[1], "Interval1 does not have the format (start, end)"
    assert interval2[0] <= interval2[1], "Interval2 does not have the format (start, end)"
    if interval1[1] <= interval2[0] or interval2[1] <= interval1[0]:
        return "NO"
    else:
        l = min(interval1[1], interval2[1])
        u = max(interval1[0], interval2[0])
        while l <= u:
            if l % 2!= 0:
                return "NO"
            else:
                l += 1
        return "YES"
