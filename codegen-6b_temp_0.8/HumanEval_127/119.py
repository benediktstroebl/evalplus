
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
    inter = interval1.start <= interval2.start <= interval1.end and interval2.start <= interval1.start <= interval1.end
    if inter:
        # define the function get_len that returns the number of 
        # elements of the intersection
        def get_len(a, b):
            i_a, i_b = interval1, interval2
            return max(min(i_a.end, i_b.end) - max(i_a.start, i_b.start), 0)
        # check that the intersection of the interval 1 and 2 is a prime number
        if is_prime(get_len(interval1, interval2)):
            return "YES"
        return "NO"
    return "NO"


