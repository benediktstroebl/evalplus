
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
    # Check if the intervals are valid
    if not (interval1.start <= interval1.end or interval2.start <= interval2.end):
        return "NO"

    # Check if the intervals intersect
    if interval1.start > interval2.end or interval2.start > interval1.end:
        return "NO"

    # Check if the intersection is a prime number
    if interval1.start < interval2.start:
        # Find the maximum value of the intersection
        max_value = max(interval1.start, interval2.start)
        # Find the first prime number greater than the maximum value
        max_index = max(interval1.start, interval2.start)
        while max_index and (max_index % max_value) == 0:
            max_index = max_index - 1
        if max_index == 0:
            return "YES"
        else:
            return "NO"
    else:
        # Find the minimum value of the intersection
        min_value = min(interval1.end, interval2.end)
        # Find the first prime number less than the minimum value
        min_index = min(interval1.end, interval2.end)
        while min_index and (min_index % min_value) == 0:
            min_index = min_index + 1
        if min_index == 0:
            return "YES"
        else:
            return "NO"
