
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
    # input
    # output
    # exmple:
    #     input 2, 6
    #     output 3, 6
    #     input 10, 20
    #     output 14, 16
    #     input 1, 100
    #     output 1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    #     input 10000, 99999
    #     output 2401, 2413, 2437, 2523, 2531, 2601, 2603, 2637, 2699, 2707, 2711, 2717, 2729, 2767, 2789, 2801, 2833, 2857, 2863, 2899, 2933, 2953, 2971, 2999

    # check
    # input:
    # output:
    #     input 2, 6
    #     output 3, 6
    #     input 10, 20
    #     output 14, 16
    #     input 1, 100
    #     output 1, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    #     input
