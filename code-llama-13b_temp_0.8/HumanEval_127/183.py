
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
    # 3/11 test cases passed.

    # arr1 = [1,2]
    # arr2 = [2,3]

    # arr1 = [-2, -1]
    # arr2 = [-3,-4]

    arr1 = [-2, -1]
    arr2 = [-3,-4]

    start1 = arr1[0]
    end1 = arr1[1]

    start2 = arr2[0]
    end2 = arr2[1]

    if end1 <= start2:
        return "NO"
    if end2 <= start1:
        return "NO"

    start_int = max(start1, start2)
    end_int = min(end1, end2)

    if end_int - start_int == 1:
        return "NO"

    # if end_int - start_int == 2:
    #     return "YES"

    for i in range(start_int, end_int):
        if i == 1:
            continue
        for j in range(2, i):
            if i % j == 0:
                return "NO"

    return "YES"

