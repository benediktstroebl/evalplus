
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
    
    def isPrime(n):
        if n < 2:
            return False
        elif n == 2:
            return True
        elif n%2 == 0:
            return False
        else:
            r = 3
            while r * r <= n:
                if n % r == 0:
                    return False
                r += 2
            return True
    
    def getInterval(interval):
        return set(range(interval[0], interval[1]+1))
    
    # 1. If the intervals are disjoint, the intersection is empty
    s1 = getInterval(interval1)
    s2 = getInterval(interval2)
    if not (s1.intersection(s2)):
        return "NO"
        
    # 2. If the intersection is a single element, intersection is a prime number
    interval = s1.intersection(s2)
    if interval and len(interval) == 1:
        return "YES"
    
    # 3. If the intersection is a prime number, the intersection is a prime number
    prime_interval = set(range(interval[0], interval[1] + 1, 2))
    if isPrime(len(prime_interval)):
        return "YES"
    
    # 4. If the intersection is not a prime number, it is a prime number
    return "NO"
    

