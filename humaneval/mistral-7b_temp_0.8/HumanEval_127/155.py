
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
    a=[]
    b=[]
    c=[]
    d=[]
    for x in range(len(interval1)):
        if interval1[x] not in a:
            a.append(interval1[x])
    for x in range(len(interval2)):
        if interval2[x] not in b:
            b.append(interval2[x])
    for x in range(len(a)):
        if a[x] in b:
            c.append(a[x])
    for x in range(len(c)):
        if c[x] in b:
            c.remove(c[x])
    for x in range(len(b)):
        if b[x] in c:
            c.remove(b[x])
    for x in range(len(c)):
        if c[x] in a:
            d.append(c[x])
    print(d)
    #write your code here
    if len(d)==0:
        return "NO"
    else:
        for x in range(len(d
