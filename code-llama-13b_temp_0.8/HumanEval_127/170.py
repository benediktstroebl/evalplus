
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

    # Your code here

    # This solution assumes the first interval is the one to check if prime.
    # The intervals are assumed to be closed, meaning the last number is included.
    # If any of the intervals are invalid (start > end), this function will fail.
    #   The start and end are considered to be integers.
    # If one of the intervals is invalid, this function will fail.
    #   An interval is considered valid if it has two integers for start and end.
    # If one of the intervals is invalid, this function will fail.
    #   An interval is considered valid if it has two integers for start and end.

    # set variables to track the start and end of the intersection, initially null
    start = None
    end = None

    # if the first interval's start is less than or equal to the second interval's start
    if interval1[0] <= interval2[0]:
        # if the first interval's end is greater than or equal to the second interval's start
        if interval1[1] >= interval2[0]:
            # set the start to the greater of the two starts
            start = max(interval1[0], interval2[0])
            # set the end to the lesser of the two ends
            end = min(interval1[1], interval2[1])
    # otherwise, if the second interval's start is less than or equal to the first interval's start
    elif interval2[0] <= interval1[0]:
        # if the second interval's end is greater than or equal to the first interval's start
        if interval2[1] >= interval1[0]:
            # set the start to the greater of the two starts
            start = max(interval2[0], interval1[0])
            # set the end to the lesser of the two ends
            end = min(interval2[1], interval1[1])
    # otherwise, the intervals don't intersect

    # if there is no start and end for the intersection,
    #   meaning the intervals don't intersect, return "NO"
    if start is None or end is None:
        return "NO"
    # otherwise, if the length of the intersection is a prime
