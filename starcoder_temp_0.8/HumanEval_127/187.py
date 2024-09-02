
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
    # 1. Compare the start of the two intervals.
    # 2. If the start of the first interval is greater, then
    # we know that the two intervals do not overlap. We return NO.
    if interval1[0] > interval2[0]:
        return "NO"

    # 3. Compare the end of the two intervals.
    # 4. If the end of the first interval is less, then we know that the two
    # intervals do not overlap. We return NO.
    if interval1[1] < interval2[1]:
        return "NO"

    # 5. The two intervals overlap.
    # 6. We compute the length of the intersection.
    # 7. If the length of the intersection is a prime number,
    # then we return YES. Otherwise, we return NO.
    interval = (interval1[1] - interval1[0]) + 1
    return "YES" if is_prime(interval) else "NO"

