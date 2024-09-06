
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

    # int(1) = 1 but int("1") = 1
    # check if the arguments are tuples
    if not isinstance(interval1, tuple) or not isinstance(interval2, tuple):
        return "NO"

    # check if the arguments are not None
    if interval1 == None or interval2 == None:
        return "NO"

    # check if the arguments have a valid value
    if len(interval1) != 2 or len(interval2) != 2:
        return "NO"

    # check if the arguments are integers
    if not isinstance(interval1[0], int) or not isinstance(interval1[1], int) or not isinstance(interval2[0], int) or not isinstance(interval2[1], int):
        return "NO"

    # check if the first interval start is bigger or equal the second interval start
    # and the first interval end is smaller or equal the second interval end
    if interval1[0] >= interval2[0] and interval1[1] <= interval2[1]:
        # check if the interval is valid
        if interval1[0] <= interval1[1] and interval2[0] <= interval2[1]:
            # check if the length of the intersection is a prime number
            # so check if the difference of the start is equal 1 or 0 and the difference of the end is equal 1 or 0
            if (interval2[0] - interval1[0] == 1 or interval2[0] - interval1[0] == 0) and (interval1[1] - interval2[1] == 1 or interval1[1] - interval2[1] == 0):
                return "YES"
    # check if the first interval start is smaller or equal the second interval start
    # and the first interval end is bigger or equal the second interval end
    elif interval1[0] <= interval2[0] and interval1[1] >= interval2[1]:
        # check if the interval is valid
        if interval1[0] <= interval1[1] and interval2[0] <= interval2[1]:
            # check if the length of the intersection is a prime number
