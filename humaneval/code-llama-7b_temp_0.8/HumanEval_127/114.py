
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
    #input validation
    if len(interval1) != 2:
        return "NO"
    if len(interval2) != 2:
        return "NO"
    
    interval1_start, interval1_end = interval1[0], interval1[1]
    interval2_start, interval2_end = interval2[0], interval2[1]
    if (interval1_start <= interval2_start <= interval1_end) or (interval1_start <= interval2_end <= interval1_end):
        intersect_start = max(interval1_start, interval2_start)
        intersect_end = min(interval1_end, interval2_end)
        if is_prime(intersect_end - intersect_start + 1):
            return "YES"
        else:
            return "NO"
    else:
        return "NO"
