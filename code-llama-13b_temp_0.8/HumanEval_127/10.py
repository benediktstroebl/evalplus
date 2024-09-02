
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

    # Interval 1 start
    i1_start = interval1[0]

    # Interval 1 end
    i1_end = interval1[1]

    # Interval 2 start
    i2_start = interval2[0]

    # Interval 2 end
    i2_end = interval2[1]

    # Intersection start
    intersect_start = max(i1_start, i2_start)

    # Intersection end
    intersect_end = min(i1_end, i2_end)

    # Intersection length
    intersect_length = intersect_end - intersect_start

    # If there is no intersection, the length is 0, return "NO"
    if intersect_length <= 0:
        return "NO"

    # If the intersection is not a prime number, return "NO"
    for i in range(2, intersect_length + 1):
        if intersect_length % i == 0:
            return "NO"

    return "YES"

