
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
    if not interval1 or not interval2:
        return "NO"
    l1, r1 = interval1
    l2, r2 = interval2
    if l1 > r2 or l2 > r1:
        return "NO"
    elif l1 > r1 and l2 > r2:
        return "NO"
    elif l1 > r2 or l2 > r1:
        return "NO"
    else:
        intersection = max(l1, l2), min(r1, r2)
        len_intersection = abs(intersection[0] - intersection[1]) + 1
        if len_intersection > 1 and len_intersection not in [i for i in range(2, len_intersection) if all(len_intersection % i != 0)]:
            return "YES"
        else:
            return "NO"
