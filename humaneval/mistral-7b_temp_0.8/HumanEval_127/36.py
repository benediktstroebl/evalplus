
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

    # 1. sort the intervals
    interval1, interval2 = sorted([interval1, interval2])
    # 2. create a list of the values for the intervals
    a, b, c, d = map(list, zip(*[interval1, interval2]))
    # 3. find the minimum and maximum values of the intervals
    min_val, max_val = min(a), max(d)
    # 4. if the min_val is greater than the max_val, return "NO"
    if min_val > max_val:
        return 'NO'
    # 5. if the min_val is equal to the max_val, return "YES"
    if min_val == max_val:
        return 'YES'
    # 6. find the length of the intersection
    # 7. check if the length of the intersection is prime
    length = (max_val - min_val) + 1
    if any(length % num == 0 for num in range(2, length)):
        return 'NO'
    return 'YES'

