
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
    start_a, end_a, start_b, end_b = interval1[0], interval1[1], interval2[0], interval2[1]
    if start_a < start_b:
        if start_b <= end_a and end_a <= end_b:
            start_c, end_c = start_b, end_a
        elif start_a <= end_b and end_b <= end_a:
            start_c, end_c = start_a, end_b
        else:
            return "NO"
    else:
        if start_a <= end_b and end_b <= end_a:
            start_c, end_c = start_a, end_b
        elif start_b <= end_a and end_a <= end_b:
            start_c, end_c = start_b, end_a
        else:
            return "NO"
    return "NO" if start_c >= end_c else str(primes(start_c, end_c))

