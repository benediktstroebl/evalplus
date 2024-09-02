
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
    # ---Solution 1: by brute-force---
    # find the intersection of two intervals
    intersect = interval1[0] if interval1[1] <= interval2[0] \
                else interval1[0] if interval1[1] >= interval2[1] \
                else interval2[0] if interval2[1] >= interval1[1] \
                else interval2[1]

    # check whether the intersection is a prime number
    if intersect == interval1[0]:
        # ---[i] means the start of interval1
        i = intersection
        # ---[j] means the start of interval2
        j = intersection
        # ---[k] means the end of interval2
        k = intersection
        # ---[l] means the end of interval1
        l = intersection
    else:
        # ---[i] means the start of interval2
        i = intersection
        # ---[j] means the start of interval1
        j = intersection
        # ---[k] means the end of interval1
        k = intersection
        # ---[l] means the end of interval2
        l = intersection

    for s, e in interval1:
        if s <= j <= e:
            j = e
        else:
            break  # out of the for-loop
    for s, e in interval2:
        if s <= i <= e:
            i = e
        else:
            break  # out of the for-loop
    for s, e in interval2:
        if s <= k <= e:
            k = e
        else:
            break  # out of the for-loop
    for s, e in interval1:
        if s <= l <= e:
            l = e
        else:
            break  # out of the for-loop

    if not (i < j or j < k or k < l):
        return "NO"
    else:
        return "YES"

