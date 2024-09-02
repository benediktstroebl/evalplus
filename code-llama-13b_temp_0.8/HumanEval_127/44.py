
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
    # Your code here
    #input: interval1 (1, 2) interval2 (2, 3)
    #output: "NO"
    #input: interval1 (-1, 1) interval2 (0, 4)
    #output: "NO"
    #input: interval1 (-3, -1) interval2 (-5, 5)
    #output: "YES"
    #O(n)
    #O(n)

    #check overlap
    start = max(interval1[0], interval2[0])
    end = min(interval1[1], interval2[1])
    # if no overlap
    if start > end:
        return "NO"

    #get length
    length = end - start + 1

    #check if prime
    count = 0
    for i in range(1, length + 1):
        if length % i == 0:
            count += 1
    if count > 2:
        return "NO"
    else:
        return "YES"

