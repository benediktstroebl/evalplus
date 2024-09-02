
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
    # print("interval1: ", interval1)
    # print("interval2: ", interval2)

    # case 1: intervals do not overlap
    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"

    # case 2: intervals overlap
    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])
    # print("intersection_start: ", intersection_start)
    # print("intersection_end: ", intersection_end)

    # now compute the length of the intersection
    intersection_length = intersection_end - intersection_start + 1
    # print("intersection_length: ", intersection_length)

    # case 3: intersection length is a prime number
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"

