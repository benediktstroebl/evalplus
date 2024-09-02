import math

def minSubArraySum(nums):
    """
    Given an array of integers nums, find the minimum sum of any non-empty sub-array
    of nums.
    Example
    minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    minSubArraySum([-1, -2, -3]) == -6
    """
    min_num = None
    min_sum = None
    for i in range(1, len(nums)):
        if nums[i-1] <= 0:
            nums[i-1] = nums[i]
        else:
            nums[i] = nums[i-1] + nums[i]

        if min_num is None:
            min_num = nums[i-1]
        if min_num > nums[i]:
            min_num = nums[i]
        if min_sum is None:
            min_sum = nums[i]
        if min_sum > nums[i]:
            min_sum = nums[i]
    return min_sum
