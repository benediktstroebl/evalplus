
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
    # Your code here

    #http://math.stackexchange.com/questions/338298/intersection-of-two-ranges
    # http://math.stackexchange.com/questions/313207/2-dimensional-intersection-of-line-segments
    # http://math.stackexchange.com/questions/242347/line-segment-intersection-points
    # http://math.stackexchange.com/questions/7374/a-few-lines-of-code-c-find-the-intersection-of-two-lines

    a = interval1

    b = interval2

    if a[1] < b[0] or b[1] < a[0]:
        return 'No'

    if a[0]<b[0] and b[1]<a[1]:
        return 'No'

    if b[0]<a[0] and a[1]<b[1]:
        return 'No'

    if a[0]<b[1]:
        x1 = a[0]
        x2 = a[1]
    else:
        x1 = b[0]
        x2 = b[1]

    y1 = a[0]*b[1] - b[0]*a[1]
    y2 = b[0]*a[1] - a[0]*b[1]

    if x2 - x1 == 0:
        if b[0] == a[0]:
            return 'Yes'
        else:
            return 'No'

    x = (y1*x2 - y2*x1)/(x2-x1)

    return 'Yes' if x>=x1 and x<=x2 else 'No'


