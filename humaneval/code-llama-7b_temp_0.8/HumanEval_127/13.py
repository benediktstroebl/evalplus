
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
    # check if the two intervals have no intersection
    if interval1[0] > interval2[1] or interval2[0] > interval1[1]:
        return "NO"
    # if they do intersect, calculate the intersection
    # get the first interval
    # check if the first number is the greater one
    if interval1[0] > interval2[0]:
        # get the second interval
        first_interval = interval2
        second_interval = interval1
    else:
        first_interval = interval1
        second_interval = interval2
    # get the intersection
    intersection = (max(first_interval[0], second_interval[0]), min(first_interval[1], second_interval[1]))
    # get the length of the intersection
    intersection_length = intersection[1] - intersection[0] + 1
    # check if it is a prime number
    if is_prime(intersection_length):
        return "YES"
    else:
        return "NO"

