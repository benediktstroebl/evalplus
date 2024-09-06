
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
    # 1st solution
    # def is_prime(x):
    #     """Return True if x is a prime number. Otherwise return False."""
    #     if x <= 1:
    #         return False
    #     for n in range(2, x):
    #         if x % n == 0:
    #             return False
    #     return True

    # def prime_interval(interval):
    #     # x, y = interval
    #     length = interval[1] - interval[0] + 1
    #     return is_prime(length)

    # if prime_interval(interval1) and prime_interval(interval2):
    #     return "YES"
    # return "NO"

    # 2nd solution
    start1, end1 = interval1
    start2, end2 = interval2
    # Find the lower bound
    if start1 <= start2:
        lower_bound = start2
    else:
        lower_bound = start1

    # Find the higher bound
    if end1 <= end2:
        higher_bound = end1
    else:
        higher_bound = end2

    # The length of the intersection is the difference between the lower_bound and higher_bound
    intersection = higher_bound - lower_bound + 1

    # Use a set to keep track of all the prime numbers.
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    prime_set = set(primes)
    return "YES" if intersection in prime_set else "NO"

