
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
    # your code here
    # return "YES" if number of bits that are 1 in both bitsets
    a, b = interval1[0], interval1[1]
    c, d = interval2[0], interval2[1]

    # get the number of bits that are 1 in both bitsets
    intervals_bit_sum = (b-a+1)*(d-c+1)
    # remove the bits that are common
    intervals_bit_sum -= len(set(range(a,b+1)).intersection(set(range(c,d+1))))

    return "YES" if is_prime(intervals_bit_sum) else "NO"
