
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
    # 80 ms; faster than 57.61%
    # def is_prime(n):
    #     if n == 1:
    #         return False
    #     if n <= 3:
    #         return True
    #     if n % 2 == 0 or n % 3 == 0:
    #         return False
    #     for i in range(5, int(n ** 0.5) + 1, 6):
    #         if n % i == 0 or n % (i + 2) == 0:
    #             return False
    #     return True

    # def intersection(interval1, interval2):
    #     a, b = interval1
    #     c, d = interval2
    #     m = max(a, c)
    #     n = min(b, d)
    #     if m > n:
    #         return 'NO'
    #     return 'YES' if is_prime(n - m + 1) else 'NO'
    
    # 64 ms; faster than 85.71%
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def intersection(interval1, interval2):
        a, b = interval1
        c, d = interval2
        m = max(a, c)
        n = min(b, d)
        if m > n:
            return 'NO'
        return 'YES' if is_prime(n - m + 1) else 'NO'
    
    # 60 ms; faster than 90.87%
    # def is_prime(n):
    #     for i in range(2, int(n ** 0.5) + 1):
    #         if n % i == 0:
    #             return False
    
