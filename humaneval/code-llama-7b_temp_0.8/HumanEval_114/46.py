import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    min_sum = math.inf
    curr_sum = 0
    start = 0
    for i, num in enumerate(nums):
        curr_sum += num
        if curr_sum < min_sum:
            min_sum = curr_sum
        elif curr_sum > 0:
            curr_sum = 0
            start = i + 1
    return min_sum

