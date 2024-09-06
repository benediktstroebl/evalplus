
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
    if interval1[0] > interval1[1] or interval2[0] > interval2[1]:
        return "NO"

    # find the closest value to the start and the closest value to the end
    # using the absolute value for the values
    interval1_start = min(abs(interval1[0]), abs(interval1[1]))
    interval1_end = max(abs(interval1[0]), abs(interval1[1]))
    interval2_start = min(abs(interval2[0]), abs(interval2[1]))
    interval2_end = max(abs(interval2[0]), abs(interval2[1]))
    # if the start value from the interval1 is less than the start value from 
    # the interval2, the intersection is already
    # also if the end value from the interval1 is greater then the end value
    # from the interval2, it means the intersection is already empty
    if interval1_start <= interval2_start or interval1_end >= interval2_end:
        return "NO"
    # if the intersection is 0, not a prime number
    if interval1_start == interval2_start and interval1_end == interval2_end:
        return "NO"
    # if the intersection is greater than 0, find the closest value to the start
    # and closest value to the end using the absolute value for the values
    intersections = abs(interval1_start - interval2_start)
    intersections += abs(interval1_end - interval2_end)

    # if the number of intersections is a prime number
    if (intersections == 1):
        return "YES"
    else:
        return "NO"
