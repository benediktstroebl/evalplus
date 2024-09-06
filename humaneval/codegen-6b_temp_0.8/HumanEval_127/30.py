
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
    def prime_number(n):
        if n < 2:
            return False
        if n == 2:
            return True
        for x in range(2, n):
            if n % x == 0:
                return False
        return True
    
    interval1 = sorted(interval1)
    interval2 = sorted(interval2)
    
    diff1 = interval1[1] - interval1[0]
    diff2 = interval2[1] - interval2[0]

    if diff1 > diff2:
        interval1, interval2 = interval2, interval1

    if interval1[0] > interval2[1]:
        return "NO"
    
    length = interval2[0] - interval1[1]
    if length > 0:
        if length in range(2,2**1000+1):
            if prime_number(length):
                return "YES"
        return "NO"
