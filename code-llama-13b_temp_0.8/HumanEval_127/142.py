
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

    # Check if both intervals are equal to each other
    if interval1 == interval2:
        return "NO"
    # Check if the first interval starts after the second
    elif interval1[0] > interval2[0] and interval1[0] > interval2[1]:
        return "NO"
    # Check if the second interval starts after the first
    elif interval2[0] > interval1[0] and interval2[0] > interval1[1]:
        return "NO"

    # Set the lower limit to be the max of the start of the two intervals
    lowerLimit = max(interval1[0], interval2[0])
    # Set the higher limit to be the min of the end of the two intervals
    higherLimit = min(interval1[1], interval2[1])

    # Get the length of the interval
    length = higherLimit - lowerLimit

    # Check if the length is a prime number
    if length == 2:
        return "YES"
    elif length > 2 and not(length % 2 == 0):
        for i in range(3, int(length / 2 + 1)):
            if length % i == 0:
                return "NO"
        return "YES"
    return "NO"

