
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
    # input: intervals
    # output: "YES"/"NO"
    # step:
    # check if intervals intersect
    # check length of intersection if prime number or not
    
    # Solution 1:
    def isprime(n):
        n = abs(n)
        # 2 is the smallest prime number
        if n <= 1:
            return False
        # iterate thru prime numbers until n/2
        for i in range(2, n//2+1):
            if n%i == 0:
                return False
        return True
    
    def intersection(interval1, interval2):
        # check if intervals intersect
        # if not, return "NO"
        if interval1[1]<interval2[0] or interval1[0]>interval2[1]:
            return "NO"
        # if intersect, compute length of intersection
        low = max(interval1[0], interval2[0])
        high = min(interval1[1], interval2[1])
        length = high - low + 1
        # check if length of intersection is prime or not
        if isprime(length):
            return "YES"
        else:
            return "NO"
    
    return intersection((1, 2), (2, 3))

