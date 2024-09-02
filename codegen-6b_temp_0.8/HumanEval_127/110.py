
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
    # brute force is to check all numbers, O(n^2)
    # logic:
    # if the intersecting point is the exact same as the end of one of the intervals
    # then return NO
    # else, if the end of one interval is greater than the start of the other interval
    # then the intersecting point is on the left side
    # if the end of one interval is less than the start of the other interval
    # then the intersecting point is on the right side

    def is_prime(num):
        if num < 2:
            return False
        elif num == 2:
            return True
        try:
            for i in range(2, num):
                if num % i == 0:
                    return False
        except TypeError:
            return True
        return True

    lst = []
    if interval1[0] < interval1[1]:
        lst.append(interval1[0])
    if interval2[0] < interval2[1]:
        lst.append(interval2[0])

    for i in lst:
        if i == interval1[1] or i == interval2[1]:
            return "NO"
        if i > min(interval1[0], interval2[0]):
            return "NO"
        elif i < max(interval1[1], interval2[1]):
            return "NO"
    return "YES"

