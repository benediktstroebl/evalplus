
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
    # Write a program that transforms a string into a new string
    # where each occurrence of some character is replaced by
    # that same character repeated n times.
    # Example:
    #   new_string("hello", 'l', 2) = "heilloo"
    #   new_string("hello", 'l', 3) = "helllllooo"

    # string = "hello"
    # char = "l"
    # n = 2
    # new_string = ""
    # if char in string:
    #     for ch in string:
    #         if ch == char:
    #             new_string += char * n
    #         else:
    #             new_string += ch
    # return new_string

    # all_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    #
    # if interval1[1] < interval2[0] or interval1[0] > interval2[1]:
    #     return "NO"
    # elif interval1[1] < interval2[1]:
    #     int_length = interval1[1] - interval2[0]
    # elif interval1[1] > interval2[1]:
    #     int_length = interval2[1] - interval2[0]
    # else:
    #     int_length = interval2[1] - interval2[0]
    #
    # if int_length in all_primes:
    #     return "YES"
    # else:
    #     return "NO"
    # # Write a function that takes an integer as input, and returns
    # # the number of bits that are equal to one in the binary
    # # representation of that number. You can assume that the input
    # # is a nonnegative integer.
