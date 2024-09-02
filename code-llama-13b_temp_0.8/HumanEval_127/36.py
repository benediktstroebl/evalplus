
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
    # your code here
    import math
    # if the interval 1 is after the interval 2
    if interval1[0] > interval2[0]:
        return intersection(interval2, interval1)
    
    # if interval 2 is after the interval 1
    if interval2[0] > interval1[1]:
        return "NO"

    # if interval 1 starts at the same place as interval 2
    if interval1[0] == interval2[0]:
        # check to see if length is prime
        if is_prime(interval1[1] - interval2[0] + 1):
            return "YES"
        else:
            return "NO"

    # if interval 1 starts before interval 2
    if interval1[0] < interval2[0]:
        # check to see if length is prime
        if is_prime(interval2[0] - interval1[0]):
            return "YES"
        else:
            return "NO"

