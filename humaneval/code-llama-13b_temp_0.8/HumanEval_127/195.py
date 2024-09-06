
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

    # in case both intervals don't intersect
    if interval1[1] < interval2[0] or interval2[1] < interval1[0]:
        return "NO"

    # determine the smaller interval
    if interval1[1] - interval1[0] <= interval2[1] - interval2[0]:
        smaller_interval = interval1
        larger_interval = interval2
    else:
        smaller_interval = interval2
        larger_interval = interval1

    # find the length of the intersection
    intersection_length = min(larger_interval[1], smaller_interval[1]) - max(
        larger_interval[0], smaller_interval[0]
    )

    # initialize the set of prime numbers
    prime_numbers = set()

    # add 2 to the set
    prime_numbers.add(2)

    # initialize the number
    number = 3

    while number <= intersection_length:
        # check if the number is prime
        if all(number % i != 0 for i in range(2, int(number ** 0.5) + 1)):
            prime_numbers.add(number)

        # increment the number
        number += 2

    # check if the length is prime
    if intersection_length in prime_numbers:
        return "YES"
    else:
        return "NO"

