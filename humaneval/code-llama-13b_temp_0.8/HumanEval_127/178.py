
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

    # can be solved with logic,
    # O(1) time complexity, and O(1) space complexity
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    start1, end1 = interval1
    start2, end2 = interval2
    length = 0

    if start1 <= start2 <= end1:
        length += start2 - start1
    elif start1 <= end2 <= end1:
        length += end2 - start1
    elif start2 <= start1 <= end2:
        length += end1 - start2
    elif start2 <= end1 <= end2:
        length += end1 - start2

    if length == 1:
        return "NO"

    if is_prime(length):
        return "YES"
    return "NO"

