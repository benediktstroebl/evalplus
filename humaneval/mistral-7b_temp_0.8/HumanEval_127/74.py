
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

    ### can't we assume that the intervals are not overlapping and the starting point is less than the ending point?
    ### that way it is easier to check if it is a prime number

    ### ok so I don't understand why we are returning no for the 2nd test case.
    ### if we take the overlap from -1 to 1, and then we take the overlap from 0 to 4
    ### wouldn't that make the overlap be from -1 to 4?
    ### if we then want to check if it is a prime number, we should just do modulo
    ### by 2 and 3, and if it is not equal to 0, then it is a prime number

    ### I'm not even sure if we should check if it is a prime number, because
    ### we should probably just check if it is negative, because if it is negative,
    ### it will be even and therefore it won't be a prime number

    ### so if the first test case is (-1, 1), and the second test case is (0, 4),
    ### then shouldn't we return "
