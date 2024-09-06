import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    length = len(nums)
    if length == 0:
        return None
    if length == 1:
        return nums[0]

    min_sum = nums[0]
    for i in range(1, length):
        if min_sum > 0:
            min_sum = min(min_sum, nums[i])
        else:
            min_sum = min(min_sum, nums[i] + min_sum)

    return min_sum
