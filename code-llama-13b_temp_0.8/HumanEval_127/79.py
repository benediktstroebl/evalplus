
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

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    # Tests if the intervals intersect
    def test_intersect(interval1, interval2):
        interval_start1 = interval1[0]
        interval_end1 = interval1[1]
        interval_start2 = interval2[0]
        interval_end2 = interval2[1]
        return (interval_start1 <= interval_end2) and (interval_end1 >= interval_start2)

    # Tests if the intervals overlap
    def test_overlap(interval1, interval2):
        interval_start1 = interval1[0]
        interval_end1 = interval1[1]
        interval_start2 = interval2[0]
        interval_end2 = interval2[1]
        return (interval_start1 < interval_end2) and (interval_end1 > interval_start2)

    def test_intersect_union(interval1, interval2):
        if test_intersect(interval1, interval2):
            return True
        elif test_overlap(interval1, interval2):
            return True
        else:
            return False

    if test_intersect_union(interval1, interval2):
        # Get intersection range
        interval_start1 = interval1[0]
        interval_end1 = interval1[1]
        interval_start2 = interval2[0]
        interval_end2 = interval2[1]
        # Check if start1 is greater than start2
        if interval_start1 > interval_start2:
            interval_start = interval_start1
        else:
            interval_start = interval_start2
        # Check if end1 is greater than end2
        if interval_end1 > interval_end2:
            interval_end = interval_end2
        else:
            interval_end = interval_end1
        # Calculate difference of ends and start
        if is_prime(interval_end - interval_start + 1):
            return "YES"
       
