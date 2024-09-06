
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
    # Version 1: Naive approach
    # max_start = max(interval1[0], interval2[0])
    # min_end = min(interval1[1], interval2[1])
    # if min_end >= max_start:
    #     start = min(interval1[0], interval2[0])
    #     end = max(interval1[1], interval2[1])
    #     length = end - start + 1
    #     if is_prime(length):
    #         return "YES"
    # return "NO"

    # Version 2: using collections.Counter
    # intervals = [interval1, interval2]
    # res = list(map(Counter, intervals))
    # for i, _ in enumerate(res):
    #     for j in range(i+1, len(res)):
    #         res[i] &= res[j]
    # if any(res[0].values()):
    #     return "YES"
    # return "NO"

    # Version 3: divide and conquer
    # start = max(interval1[0], interval2[0])
    # end = min(interval1[1], interval2[1])
    # if start <= end:
    #     return "YES" if is_prime(end - start + 1) else "NO"
    # return "NO"

    # Version 4: math way
    # return "YES" if not any(map(is_prime, map(lambda i: i[1] - i[0] + 1, [interval1, interval2]))) else "NO"
    
    # Version 5: one liner
    return "YES" if not any(map(is_prime, map(lambda i: i[1] - i[0] + 1, [interval1, interval2]))) else "NO"

