
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

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True
    
    # If the two intervals don't intersect, return "NO".
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return 'NO'

    # The intersection begins from the highest of the two intervals' start points,
    # and ends at the lowest of the two intervals' end points.
    intersection_start = max(interval1[0], interval2[0])
    intersection_end = min(interval1[1], interval2[1])

    # The intersection length is the number of integers between the highest of the 
    # two intervals' start points, and the lowest of the two intervals' end points,
    # plus 1. 
    intersection_length = intersection_end - intersection_start + 1
    
    # If the length of the intersection is a prime number, return "YES", 
    # otherwise, return "NO".
    return 'YES' if is_prime(intersection_length) else 'NO'


    # Alternatively, use numpy.intersect1d:
    import numpy as np
    
    a = np.array(interval1)
    b = np.array(interval2)
    intersection = np.intersect1d(a, b)
    return 'YES' if is_prime(len(intersection)) else 'NO'


    # Alternatively, use set()
    a = set(range(interval1[0], interval1[1]+1))
    b = set(range(interval2[0], interval2[1]+1))
    intersection = a.intersection(b)
    return 'YES' if is_prime(len(intersection)) else 'NO'


