
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
    if interval1[0] < interval1[1]:
        if interval2[0] < interval2[1]:
            if interval1[0] <= interval2[0] <= interval2[1] <= interval1[1]:
                return "NO"
            else:
                if interval2[0] <= interval1[0] <= interval1[1] <= interval2[1]:
                    return "NO"
                else:
                    return "NO"
        else:
            if interval2[0] <= interval1[0] <= interval1[1] <= interval2[0]:
                return "NO"
            else:
                if interval1[0] <= interval2[0] <= interval2[1] <= interval1[1]:
                    return "NO"
                else:
                    return "NO"
    else:
        if interval2[0] < interval2[1]:
            if interval2[0] <= interval1[0] <= interval1[1] <= interval2[1]:
                return "NO"
            else:
                if interval1[0] <= interval2[0] <= interval2[1] <= interval1[1]:
                    return "NO"
                else:
                    return "NO"
        else:
            if interval1[0] <= interval2[0] <= interval2[1] <= interval1[1]:
                return "NO"
            else:
                if interval2[0] <= interval1[0] <= interval1[1] <= interval2[1]:
                    return "NO"
                else:
                    return "NO"
    int1 = interval1[0]
    int2 = interval1[1]
    int3 = interval2[0]
    int4 = interval2[1]
    if (int1 <= int3 <= int2 and int1 <= int4 <= int2) or (int3 <= int1 <= int4 and int3 <= int2 <= int4):
        ints = list()
        ints.append(int(max(int1, int3)))
        ints.append(int(min(int2, int4)))
        if ints[0] <= ints[1]:
           
