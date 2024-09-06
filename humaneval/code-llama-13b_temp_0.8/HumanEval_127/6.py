
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

    # NOTE: WE DO NOT NEED TO CHECK IF ENDS ARE EQUAL.
    # INTERVALS ARE CLOSED, SO THEY INCLUDE BOTH ENDS.
    # ALSO, WE DON'T NEED TO CHECK IF STARTS ARE EQUAL.
    # THEY WILL ALWAYS BE DIFFERENT, OTHERWISE THEY WOULDN'T INTERSECT.
    if (interval1[1] < interval2[0]) or (interval2[1] < interval1[0]):
        return "NO"

    # THIS IS THE INTERVAL OF THE TWO INTERVALS.
    # IF IT IS EMPTY, THEY DO NOT INTERSECT.
    # OTHERWISE, THEY INTERSECT AND THE LENGTH IS A PRIME.
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])

    if start > end:
        return "NO"

    return "YES"

