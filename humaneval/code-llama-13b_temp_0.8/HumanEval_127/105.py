
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
    # Write your code here
    # let's start by checking if the two intervals actually intersects
    # in order to do so, let's check if interval1 is to the right of interval2
    # and if interval2 is to the right of interval1
    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"
    # now, check if the length of the intersecting part is prime
    # to do so, let's get the maximum and minimum between the two intervals
    # and then calculate the length of the interval
    minInterval, maxInterval = max(
        interval1[0], interval2[0]), min(interval1[1], interval2[1])
    length = maxInterval - minInterval + 1
    # now, check if the length is prime
    # for that, we will check if there are any numbers between 2 and sqrt(length)
    # that divides length
    for i in range(2, int(math.sqrt(length))):
        if length % i == 0:
            return "NO"
    return "YES"
