
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
    assert isinstance(interval1, tuple)
    assert isinstance(interval2, tuple)

    if interval1[0] > interval1[1]: # swap the start and the end
        interval1 = (interval1[1], interval1[0])

    if interval2[0] > interval2[1]: # swap the start and the end
        interval2 = (interval2[1], interval2[0])

    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"

    #Condition1
    if (interval1[1] <= interval2[0] or interval1[0] >= interval2[1]) :
        return "NO"

    #Condition 2
    if ((interval1[0] < interval2[0]) and (interval2[0] < interval1[1])) and ((interval1[1] > interval2[1])):
        return "NO"

    #Condition 3
    if (interval1[0] == interval2[0]) or (interval1[1] == interval2[1]):
        return "YES"

    #Condition 4
    if interval2[0] == interval1[0]:
        return "NO"

    #Condition 5
    if interval2[1] == interval1[1]:
        return "NO"

    #Length of the intersection
    return str(abs(interval1[1]-interval2[0])-abs(interval1[0]-interval2[1]))