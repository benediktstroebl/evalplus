import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    sum = float("inf")
    start = 0
    min_sum = float("inf")
    for end in range(len(nums)):
        sum = sum - nums[start] + nums[end]
        if sum <= min_sum:
            min_sum = sum
        if sum < 0:
            sum = 0
            start = end
    return sum if min_sum
