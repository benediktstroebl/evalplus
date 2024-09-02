import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """

    if len(nums) == 1:
        return nums[0]

    sum_left = math.inf
    min_sum = math.inf
    for num in nums:
        sum_left = min(sum_left, num)
        min_sum = min(min_sum, sum_left)

    return min_sum
