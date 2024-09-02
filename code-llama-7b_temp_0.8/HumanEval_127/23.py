
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

    #For the first case, the intersection of the intervals (1, 3) and (2, 4)
    #is (2, 3), which its length is 1, which not a prime number.
    if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
        return "NO"
    #For the second case, the intersection of the intervals (-1, 1) and (0, 4)
    #is empty, so it doesn't intersect.
    elif interval1[0] > interval2[1] or interval1[1] < interval2[0]:
        return "NO"
    #For the third case, the intersection of the intervals (-3, -1) and (-5, 5)
    #is (-3, -1), which its length is 2 which is a prime number.
    else:
        temp_interval = [max(interval1[0], interval2[0]), min(interval1[1], interval2[1])]
        print("temp_interval[0]", temp_interval[0])
        print("temp_interval[1]", temp_interval[1])
        length = temp_interval[1] - temp_interval[0] + 1
        if length == 1:
            return "NO"
        for i in range(2, length):
            if length % i == 0:
                return "NO"
        return "YES"
