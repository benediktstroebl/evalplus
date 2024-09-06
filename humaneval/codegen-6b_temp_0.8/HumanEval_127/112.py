
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
    
    # Convert interval into a string which is easier to compare
    inter1 = str_interval(interval1)
    inter2 = str_interval(interval2)
    
    # Check if there is an overlap or not
    if inter1[0] > inter2[1]:
        # No overlaps
        return "NO"
    elif inter1[1] < inter2[0]:
        # No overlaps
        return "NO"
    elif inter1[0] == inter2[0] and inter1[1] == inter2[1]:
        # The intervals are the same
        return "NO"
    else:
        # There is an overlap
        return "YES"

