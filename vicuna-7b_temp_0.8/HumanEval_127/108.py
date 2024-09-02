
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
    if interval1[0] < interval1[1] or interval2[0] < interval2[1]:
        return "NO"
    else:
        start1 = interval1[0]
        end1 = interval1[1]
        start2 = interval2[0]
        end2 = interval2[1]
        intersection = [start1, end1, start2, end2]
        length = len(intersection)
        if length % 2 == 0:
            return "NO"
        else:
            for i in range(1, length-1):
                if (intersection[i] % (intersection[i-1]) == 0 or (intersection[i] % (intersection[i+1] - 1)) == 0):
                    return "NO"
            return "YES"



test_cases = [
    ("(1, 2), (2, 3)", "NO"),
    ("(-1, 1), (0, 4)", "NO"),
    ("(-3, -1), (-5, 5)", "YES"),
    ("(1, 10), (5, 15)", "YES"),
    ("(10, 1), (5, 15)", "YES")
]

for test_case in test_cases:
    interval1, interval2 = test_case[0].split(", ")
    result = intersection(interval1, interval2)
    print(test_case[0])
    print(result)